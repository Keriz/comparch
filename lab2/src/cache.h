#ifndef CACHE_H
#define CACHE_H

#include "mc_definitions.h"
#include <stdint.h>

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
#define BLOCK_MASK  (UINT32_MAX ^ ((1 << 6) - 1))
#define BLOCK_EMPTY -1

typedef enum cache_state
{
	NO_MISS,
	CACHE_HIT_L2,
	DELAY_MC_PIPE_MW,
	DELAY_MC_PIPE_MR,
	WAIT_FILL_NOTIF,
	FILL_NOTIF_RECEIVED,
	INSERT_CACHE_BLOCK
} Cache_state;

//Miss-status holding registers
typedef struct MSHR {
	uint8_t valid_bit;
	int addr_cache_block_miss;
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
	Cache_state state;
	MSHR mshrs[MAX_NB_MSHR];
} Cache;

extern Cache *instruction_cache, *data_cache, *unified_l2_cache;

//Returns a pointer to a cache
Cache *cache_init(uint32_t cache_size, uint32_t block_size, uint8_t associativity);
void cache_deinit(Cache *);
void cache_free_mshr(Cache *, uint32_t addr);
void cache_allocate_mshr(Cache *, uint32_t addr, uint32_t cycle, Req_stage_origin origin);
uint8_t cache_mshrs_left(Cache *);
Cache_response cache_request(Cache *, uint32_t addr);
void cache_insert(Cache *, uint32_t addr);
void cache_l2_fill_notification(Cache *c, uint32_t addr, uint8_t origin);
void cache_fill_notification(Cache *c);

#endif