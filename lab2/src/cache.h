#ifndef CACHE_H
#define CACHE_H

typedef enum Cache_response
{
	miss,
	hit
} Cache_response;

#define FLAG_DIRTY_DATA     0
#define FLAG_UNTOUCHED_DATA 1

#define FLAG_INVALID_DATA 0
#define FLAG_VALID_DATA   1

#define FULLY_ASSOCIATIVE 0x00
#define DIRECT_MAPPED     0x01
#define FOUR_WAY          0x04

#define MAX_NB_MSHR 16

#include <math.h>
#include <stdint.h>

//Miss-status holding registers

enum l2_miss_state
{
	NO_MISS,
	DELAY_MEM_CONTROLLER,
	CACHE_BLOCK_BEING_INSERTED,
	CACHE_HIT
} l2_miss_state_t;

typedef struct MSHR {
	uint8_t valid_bit;
	uint32_t addr_cache_block_miss;
	uint8_t done_bit;
} MSHR;

// implentation of a set-associative cache
typedef struct Cache_line {
	uint32_t tag; //tag_length = address_length - index_length - block_offset_length
	uint8_t d_flag;
	uint8_t v_flag;
	uint16_t recency; //for the Least Recently Accessed policy
} Cache_line;

typedef struct Cache_set {
	Cache_line *ways;
} Cache_set;

typedef struct Cache {
	uint32_t cache_size;
	uint32_t block_size;
	uint8_t associativity;
	uint16_t nb_sets;
	uint32_t tag_mask;
	Cache_set *sets;
	MSHR mshrs[MAX_NB_MSHR];
} Cache;

extern Cache *instruction_cache, *data_cache, *unified_l2_cache;

//Returns a pointer to a cache
Cache *cache_init(uint32_t cache_size, uint32_t block_size, uint8_t associativity);
void cache_deinit(Cache *);
void cache_free_mshr(Cache *, uint32_t);
void cache_allocate_mshr(Cache *, uint32_t);
uint8_t cache_mshrs_left(Cache *);
Cache_response cache_request(Cache *, uint32_t);
void cache_insert(Cache *, uint32_t);
#endif