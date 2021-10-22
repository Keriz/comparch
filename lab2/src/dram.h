#ifndef DRAM_H
#define DRAM_H

#include <stdint.h>

#define NB_ROWS  64000
#define NB_BANKS 1 << 3
#define ROW_SIZE 1 << 13 //(8024*1B)

enum dram_commands
{
	ACTIVATE,
	READ,
	WRITE,
	PRECHARGE
} dram_commands;

enum row_buffer_states
{
	RB_HIT,
	RB_MISS,
	RB_CONFLICT
} row_buffer_states;

enum bank_states
{
	BANK_BUSY,
	BANK_FREE
} bank_states;

typedef enum bus_states
{
	BUS_FREE,
	BUS_BUSY
} bus_state;

typedef struct row_struct {
	uint8_t data[ROW_SIZE];
} Row;

typedef struct bank_struct {
	Row rows[NB_ROWS];
	Row row_buffer;
	uint16_t counter;
} Bank;

typedef struct bus_struct {
	uint16_t counter;
	bus_state cycles[250];
} Bus;

typedef struct dram_struct {
	//since there is only 1 rank, 1 channel, lets write everything in here
	Bank banks[NB_BANKS];
	Bus cmd_bus, data_bus, address_bus;
} Dram;

typedef struct request_t {
	struct request_t *next, *prev;
} Request;

Request *req_queue;

extern Dram dram;

void dram_initialize();
void dram_deinitialize();
void dram_mc_scan_queue();
#endif