#include "cache.h"
#include "shell.h"

#include <stdio.h>
#include <stdlib.h>

#define V_FLAG 1 << 0
#define D_FLAG 1 << 1 //dirty flag

#define INVALID_ALLOCATION   1
#define INCORRECT_PARAMETERS 2
#define INVALID_POINTER      3

//extern
Cache *instruction_cache, *data_cache;

static inline uint32_t c_log2(uint32_t v) {
	return 31 - __builtin_clzl(v);
}

size_t least_recently_accessed_policy(Cache *c, const uint16_t set) {
	if (!c) exit(INVALID_POINTER);
	for (size_t i = 0; i < c->associativity; i++) {
		if (c->sets[set].lines[i].recency == 0) {
			return i;
		}
	}
}

void update_access_age(Cache *c, const uint16_t set, const uint16_t line_index) {
	if (c->sets[set].lines[line_index].recency == 3) return;

	c->sets[set].lines[line_index].recency = 3;
	for (size_t i = 0; (i < c->associativity) && i != line_index; i++) {
		c->sets[set].lines[i].recency--;
		if (c->sets[set].lines[i].recency >= c->associativity)
			c->sets[set].lines[i].recency = 0;
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
		c->sets[i].lines = malloc(sizeof(Cache_line) * c->associativity);
		if (!c->sets[i].lines) exit(INVALID_ALLOCATION);

		/* c->sets[i].lines->data = malloc(sizeof(uint8_t) * c->block_size);
		if (!c->sets[i].lines->data) exit(INVALID_ALLOCATION); */

		//set all cache tags to invalid
		for (size_t j = 0; j < c->associativity; j++) {
			c->sets[i].lines[j].v_flag = 0;
			c->sets[i].lines[j].tag    = 0;
		}
	}

	return c;
}

Cache_response cache_access(Cache *c, uint32_t addr) {
	if (!c) exit(INVALID_POINTER);

	uint8_t set_offset  = c_log2(c->block_size);
	uint8_t tag_offset  = c_log2(c->block_size) + c_log2(c->nb_sets);
	uint16_t tag        = (addr << 20) >> 20 >> tag_offset;
	uint16_t set        = (addr >> set_offset) & ((1 << c_log2(c->nb_sets)) - 1);
	uint16_t line_index = 0;

	uint8_t cached = 0;

	for (size_t i = 0; i < c->associativity; i++) {
		//already in cache, nothing to do
		if (c->sets[set].lines[i].tag == tag) {
			line_index = i;
			if (!c->sets[set].lines[i].v_flag) {
				c->sets[set].lines[i].v_flag = 1;
				line_index                   = i;
				cached                       = miss;
				break;
			}
			cached = hit;
		}
	}

	update_access_age(c, set, line_index);

	if (!cached) {
		//increment cycles by 51, if d flag, write back, otherwise just load new memory
		return miss;

		if (c->sets[set].lines[line_index].d_flag) {
			//mem_write_32(addr, c->sets[set].lines[line_index].data);
		}
		//c->sets[set].lines[line_index].data = mem_read_32(addr);

	} else {
		//return c->sets[set].lines[line_index].data;
		return hit;
	}
}