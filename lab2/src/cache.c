#include "cache.h"
#include "dram.h"
#include "shell.h"

#include <stdio.h>
#include <stdlib.h>

#define INVALID_ALLOCATION   1
#define INCORRECT_PARAMETERS 2
#define INVALID_POINTER      3

//extern
Cache *instruction_cache, *data_cache, *unified_l2_cache;

static inline uint32_t c_log2(uint32_t v) {
	return 31 - __builtin_clzl(v);
}

size_t least_recently_used_policy(Cache *c, const uint16_t set) {
	if (!c) exit(INVALID_POINTER);
	for (size_t i = 0; i < c->associativity; i++) {
		if (c->sets[set].ways[i].recency == 0) {
			return i;
		}
	}
}

void update_access_recency(Cache *c, const uint16_t set, const size_t way_index) {
	if (!c) exit(INVALID_POINTER);
	if (c->sets[set].ways[way_index].recency == 3) return;

	c->sets[set].ways[way_index].recency = 3;
	for (size_t i = 0; i < c->associativity; i++) {
		if (i == way_index) continue;
		c->sets[set].ways[i].recency--;
		if (c->sets[set].ways[i].recency >= c->associativity)
			c->sets[set].ways[i].recency = 0;
	}
}

Cache *cache_init(uint32_t cache_size, uint32_t block_size, uint8_t associativity) {

	if (!cache_size || !block_size) exit(INCORRECT_PARAMETERS);
	Cache *c = malloc(sizeof(Cache));
	if (!c) exit(INVALID_ALLOCATION);
	c->block_size = block_size;
	c->cache_size = cache_size;

	c->nb_sets = cache_size >> c_log2(associativity) >> c_log2(block_size);
	if (!c->nb_sets) exit(INCORRECT_PARAMETERS);

	c->sets = malloc(sizeof(Cache_set) * c->nb_sets);
	if (!c->sets) exit(INVALID_ALLOCATION);

	//FULLY ASSOCIATIVE?
	if (!associativity)
		associativity != associativity; //set to max n-ways

	c->associativity = associativity;

	for (size_t i = 0; i < c->nb_sets; ++i) {
		c->sets[i].ways = malloc(sizeof(Cache_line) * c->associativity);
		if (!c->sets[i].ways) exit(INVALID_ALLOCATION);

		/* c->sets[i].ways->data = malloc(sizeof(uint8_t) * c->block_size);
		if (!c->sets[i].ways->data) exit(INVALID_ALLOCATION); */

		//set all cache tags to invalid
		for (size_t j = 0; j < c->associativity; j++) {
			c->sets[i].ways[j].v_flag  = 0;
			c->sets[i].ways[j].tag     = 0;
			c->sets[i].ways[j].recency = 0;
		}
	}

	for (size_t i; i < MAX_NB_MSHR; ++i) {
		c->mshrs[i].addr_cache_block_miss = BLOCK_EMPTY;
		c->mshrs[i].valid_bit             = 0;
		c->mshrs[i].done_bit              = 0;
	}

	return c;
}

void cache_deinit(Cache *c) {
	for (size_t i = 0; i < c->nb_sets; i++) {
		free(c->sets[i].ways);
	}

	free(c->sets);
	free(c);
}

Cache_response cache_request(Cache *c, uint32_t addr) {
	if (!c) exit(INVALID_POINTER);

	uint8_t set_offset = c_log2(c->block_size);
	uint8_t tag_offset = c_log2(c->block_size) + c_log2(c->nb_sets);
	uint32_t tag       = addr >> tag_offset;
	uint32_t set       = (addr >> set_offset) & ((1 << c_log2(c->nb_sets)) - 1);
	uint16_t way_index = 0;

	for (size_t i = 0; i < c->associativity; i++) {
		//already in cache, nothing to do
		way_index = i;
		if (!c->sets[set].ways[i].v_flag) {
			/* 			c->sets[set].ways[i].v_flag = 1;
			c->sets[set].ways[i].tag    = tag; */
			/* update_access_recency(c, set, way_index); */
			return miss;
		} else if (c->sets[set].ways[i].tag == tag) {
			update_access_recency(c, set, way_index);
			return hit;
		}
	}
	//if we're here, that's a miss!
	//increment cycles by 51, if d flag, write back, otherwise just load new memory
	/* 	if (c->sets[set].ways[way_index].d_flag) {
	} */
	/* 	size_t lru                 = least_recently_used_policy(c, set); //pick the LRU way in the set, where our new block will be
	c->sets[set].ways[lru].tag = tag;
	update_access_recency(c, set, lru); */
	return miss;
}

void cache_insert(Cache *c, uint32_t addr) {
	if (!c) exit(INVALID_POINTER);

	uint8_t set_offset = c_log2(c->block_size);
	uint8_t tag_offset = c_log2(c->block_size) + c_log2(c->nb_sets);
	uint32_t tag       = addr >> tag_offset;
	uint32_t set       = (addr >> set_offset) & ((1 << c_log2(c->nb_sets)) - 1);
	uint16_t way_index = 0;

	for (size_t i = 0; i < c->associativity; i++) {
		//already in cache, nothing to do
		way_index = i;
		if (!c->sets[set].ways[i].v_flag) {
			c->sets[set].ways[i].v_flag = 1;
			c->sets[set].ways[i].tag    = tag;
			update_access_recency(c, set, way_index);
		} /* else if (c->sets[set].ways[i].tag == tag) {
			update_access_recency(c, set, way_index);
		} */
	}
	//if we're here, that's a miss!
	//increment cycles by 51, if d flag, write back, otherwise just load new memory
	/* 	if (c->sets[set].ways[way_index].d_flag) {
	} */
	size_t lru                 = least_recently_used_policy(c, set); //pick the LRU way in the set, where our new block will be
	c->sets[set].ways[lru].tag = tag;
	update_access_recency(c, set, lru);
}

void cache_free_mshr(Cache *c, uint32_t addr) {
	for (size_t i = 0; i < MAX_NB_MSHR; i++) {
		if (c->mshrs[i].addr_cache_block_miss == (addr & BLOCK_MASK)) {
			c->mshrs[i].addr_cache_block_miss = BLOCK_EMPTY;
			c->mshrs[i].valid_bit             = 0;
			c->mshrs[i].done_bit              = 0;
		}
	}
}

void cache_allocate_mshr(Cache *c, uint32_t addr, uint32_t cycle, Req_stage_origin origin) {
	for (size_t i = 0; i < MAX_NB_MSHR; i++) {
		if (c->mshrs[i].addr_cache_block_miss == BLOCK_EMPTY) {
			c->mshrs[i].addr_cache_block_miss = addr & BLOCK_MASK;
			c->mshrs[i].done_bit              = 0;
			c->mshrs[i].valid_bit             = 0;
			dram_mc_issue_request(addr, cycle, origin);
			return;
		}
	}
}

uint8_t cache_mshrs_left(Cache *c) {
	uint8_t counter = 0;
	for (size_t i = 0; i < MAX_NB_MSHR; i++) {
		if (c->mshrs[i].addr_cache_block_miss != BLOCK_EMPTY) {
			counter++;
		}
	}

	return (counter == MAX_NB_MSHR) ? 0 : 1;
}
