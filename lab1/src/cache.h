#ifndef CACHE_H
#define CACHE_H

#include <stdlib.h>

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

#include <math.h>
#include <stdint.h>

// implentation of a set-associative cache
typedef struct Cache_line {
	//uint8_t *data;
	uint8_t tag; //tag_length = address_length - index_length - block_offset_length
	uint8_t d_flag;
	uint8_t v_flag;
	uint16_t lru; //for the Least Recently Accessed policy
} Cache_line;

typedef struct Cache_set {
	Cache_line *lines;
} Cache_set;

typedef struct Cache {
	uint32_t cache_size;
	uint32_t block_size;
	uint8_t associativity;
	uint16_t nb_sets;
	uint32_t tag_mask;
	Cache_set *sets;
} Cache;

extern Cache instruction_cache, data_cache;

uint32_t cache(Cache *, uint32_t);
Cache_response cache_access(Cache *, uint32_t);
#endif