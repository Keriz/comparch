#ifndef DRAM_H
#define DRAM_H

#include "mc_definitions.h"
#include <stdint.h>

#define NB_ROWS    64000
#define NB_BANKS   1 << 3
#define ROW_SIZE   1 << 13 //(8024*1B)
#define BANK_MASK  0xe0
#define ROW_MASK   0xffff0000
#define ROW_CLOSED -1

typedef enum Dram_command
{
	PRECHARGE,
	ACTIVATE,
	READ_WRITE,
} Dram_command;

typedef enum req_states
{
	REQ_UNASSIGNED,
	REQ_ASSIGNED
} Req_state;

typedef struct request_t {
	struct request_t *next, *prev;
	uint32_t addr, cycle, origin;
	Req_state state;
	uint8_t cmd_index;
	Dram_command cmds_to_issue[4];
} Request;

Request *req_queue;

typedef enum row_buffer_resp
{
	RB_HIT,
	RB_MISS,
	RB_CONFLICT
} Row_buffer_states;

/* typedef struct row_struct {
	//uint8_t data[ROW_SIZE];

} Row; */

typedef long int Row;

typedef struct bank_struct {
	Row rows[NB_ROWS];
	Row row_buffer;
	uint16_t counter;
	Dram_command lastcmd;
} Bank;

typedef struct bus_struct {
	uint16_t counter;
} Bus;

typedef struct dram_struct {
	//since there is only 1 rank, 1 channel, lets write everything in here
	Bank banks[NB_BANKS];
	Request *bank_requests[NB_BANKS];
	Bus cmd_bus, data_bus, address_bus;
} Dram;

extern Dram dram;

void dram_initialize();
void dram_deinitialize();
void dram_cycle();
void dram_mc_issue_request(uint32_t addr, uint32_t cycle, Req_stage_origin origin);
#endif