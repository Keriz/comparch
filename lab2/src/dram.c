#include "dram.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

Dram dram;

Request *add_req(uint32_t addr, uint32_t cycle, uint32_t origin);
Request *queue_get_last();
void remove_req(Request *r);

void dram_access(Request *r);
uint8_t dram_is_req_issuable(Request *r, uint8_t bank_index);
void dram_issue_command(Request *r, uint8_t bank_index);
Row_buffer_states dram_rb_actions(uint8_t bank_i, uint32_t row);
Request *fr_fcfs_policy(size_t bank_i);

void dram_initialize(Cache *l2) {
	for (size_t i = 0; i < NB_BANKS; i++) {
		//memset(dram.bank[i].rows, 0, sizeof(Row) * NB_ROWS);
		dram.bank[i].row_buffer  = ROW_CLOSED;
		dram.bank[i].current_req = NULL;
	}
	dram.l2   = l2;
	req_queue = NULL;
}

void dram_deinitialize() {
	Request *r = queue_get_last();
	if (r != NULL) {
		while (r->prev != NULL) {
			r = r->prev;
			free(r->next);
		}

		free(r);
	}
	req_queue = NULL;
}

void dram_mc_issue_request(uint32_t addr, uint32_t cycle, Req_stage_origin origin) {
	//create request
	add_req(addr, cycle, origin);
	/* 
	switch ()
		uint8_t bank_i = addr & BANK_MASK;
	dram->bank[bank_i]; */
}

void remove_req(Request *r) {
	if (!r) exit(3);

	if (r->prev != NULL)
		r->prev->next = r->next;
	if (r == req_queue)
		if (r->next) {
			req_queue     = r->next;
			r->next->prev = NULL;
		} else
			req_queue = NULL;
	free(r);
}

Request *add_req(uint32_t addr, uint32_t cycle, uint32_t origin) {
	Request *new_r;
	if (req_queue == NULL) {
		req_queue = malloc(sizeof(Request));
		new_r     = req_queue;
		if (!new_r) exit(3);
		new_r->prev = NULL;

	} else {
		new_r = malloc(sizeof(Request));
		if (!new_r) exit(3);
		Request *last = queue_get_last();
		new_r->prev   = last;
		last->next    = new_r;
	}

	new_r->addr      = addr;
	new_r->cycle     = cycle;
	new_r->origin    = origin;
	new_r->next      = NULL;
	new_r->state     = REQ_UNASSIGNED;
	new_r->cmd_index = 0;

	for (size_t i = 0; i < 4; i++) {
		new_r->cmds_to_issue[i] = NO_COMMAND;
	}

	return new_r;
}

Request *queue_get_last() {
	Request *r = req_queue;
	while (r && r->next != NULL)
		r = r->next;
	return r;
}

/*
Scan the request queue to find the next schedulable one, if any
*/
void dram_cycle() {
	if (dram.cmd_bus.counter > 0) dram.cmd_bus.counter--;
	if (dram.address_bus.counter > 0) dram.address_bus.counter--;
	if (dram.data_bus.counter > 0) {
		dram.data_bus.counter--;
		if (dram.data_bus.counter == 0) {
			cache_l2_fill_notification(dram.l2, dram.data_bus.current_req->addr, dram.data_bus.current_req->origin);
			remove_req(dram.data_bus.current_req);
			dram.data_bus.current_req = NULL;
		}
	}

	//update cycle for each bank if needed
	for (size_t i = 0; i < NB_BANKS; i++) {
		if (dram.bank[i].counter > 0)
			dram.bank[i].counter--;

		if (dram.bank[i].counter == 0) {

			if (dram.bank[i].lastcmd == READ_WRITE) {
				dram.data_bus.counter     = 50;
				dram.bank[i].lastcmd      = DATA;
				dram.data_bus.current_req = dram.bank[i].current_req;
				return;
			}
			//is there any next actions for the ongoing request?
			if (dram.bank[i].current_req != NULL) {
				dram_issue_command(dram.bank[i].current_req, i);
			} else {
				//is there a new request to issue for this bank?
				Request *req_to_issue = fr_fcfs_policy(i);
				if (req_to_issue == NULL) return;
				uint8_t row = (req_to_issue->addr & ROW_MASK) >> 16;

				//find out what commands would need to be sent for that request
				switch (dram_rb_actions(i, row)) {
					case RB_HIT:
						req_to_issue->cmds_to_issue[0] = READ_WRITE;
						break;
					case RB_MISS:
						req_to_issue->cmds_to_issue[0] = ACTIVATE;
						req_to_issue->cmds_to_issue[1] = READ_WRITE;
						break;
					case RB_CONFLICT:
						req_to_issue->cmds_to_issue[0] = PRECHARGE;
						req_to_issue->cmds_to_issue[1] = ACTIVATE;
						req_to_issue->cmds_to_issue[2] = READ_WRITE;
						break;
				}

				if (dram_is_req_issuable(req_to_issue, i)) {
					req_to_issue->state      = REQ_ASSIGNED;
					dram.bank[i].current_req = req_to_issue;
					dram_issue_command(dram.bank[i].current_req, i);
				}
			}
		}
	}
}

//for each paper

uint8_t dram_is_req_issuable(Request *r, uint8_t bank_index) {
	uint32_t next_cycles_data[500] = {0}, next_cycles_cmd[500] = {0}, next_cycles_addr[500] = {0};

	memset(next_cycles_data, dram.data_bus.counter * sizeof(uint32_t), 10);
	memset(next_cycles_cmd, dram.cmd_bus.counter * sizeof(uint32_t), 10);
	memset(next_cycles_addr, dram.address_bus.counter * sizeof(uint32_t), 10);

	for (size_t i = 0; i < NB_BANKS; i++) {
		Request *tmp  = dram.bank[i].current_req;
		uint32_t cntr = dram.bank[i].counter;

		if (tmp == NULL) continue;
		for (size_t j = tmp->cmd_index; j < 4; j++) {
			memset(next_cycles_addr + (j * 100 + cntr) * sizeof(uint32_t), 50 * sizeof(uint32_t), i + 1);
			memset(next_cycles_cmd + (j * 100 + cntr) * sizeof(uint32_t), 50 * sizeof(uint32_t), i + 1);

			if (tmp->cmds_to_issue[j] == READ_WRITE) {
				memset(next_cycles_data + (j * 100 + cntr) * sizeof(uint32_t), 50 * sizeof(uint32_t), i + 1);
				break;
			}
			//TODO: take care of the case when a req is issued at the same time the last one finished
		}
	}

	//for each cycle check if it is a free slot or not..
	for (size_t i = 0; i < 4; i++) {
		for (size_t j = 0; j < 4; j++) {
			if (next_cycles_addr[i * 100 + j])
				return 0;
			if (next_cycles_data[i * 100 + j])
				return 0;
		}

		if (r->cmds_to_issue[i] == READ_WRITE) {
			for (size_t j = 0; j < 50; j++)
				if (next_cycles_data[(i + 1) * 100 + j])
					return 0;
			break;
		}
	}

	/* 	printf("addr_bus: ");
	for (size_t i = 0; i < 500; i++)
		if (next_cycles_addr[i])
			printf("%lu ", next_cycles_addr[i]);
	printf("\ncmd_bus: ");
	for (size_t i = 0; i < 500; i++)
		if (next_cycles_cmd[i])
			printf("%lu ", next_cycles_cmd[i]);
	printf("\ndata_bus: ");
	for (size_t i = 0; i < 500; i++)
		if (next_cycles_data[i])
			printf("%lu ", next_cycles_data[i]);
	printf("\n"); */

	return 1;
}

void dram_issue_command(Request *r, uint8_t bank_index) {
	dram.cmd_bus.counter         = 4;
	dram.address_bus.counter     = 4;
	dram.cmd_bus.current_req     = r;
	dram.address_bus.current_req = r;

	/* switch (r->cmds_to_issue[r->cmd_index]) { //for future use
		case PRECHARGE:
			break;
		case ACTIVATE:
			break;
		case READ_WRITE:
			break;
	} */

	dram.bank[bank_index]
	    .lastcmd                     = r->cmds_to_issue[r->cmd_index];
	dram.bank[bank_index].row_buffer = r->addr & ROW_MASK;
	dram.bank[bank_index].counter    = 100;

	r->cmd_index++;
}

/*
1. Requests that are row buffer hits are prioritized over others
2. Requests that arrived earlier are prioritized over others
3. Requests coming from the memory stage are priorized over others
*/
Request *fr_fcfs_policy(size_t bank_i) {
	Request *r_to_schedule = NULL, *r = req_queue;
	Request *bank_req[1000]        = {NULL};
	Request *row_buffer_hits[1000] = {NULL};
	uint32_t nb_hits = 0, nb_req = 0;

	if (!r) return NULL; //no requests to take care of

	//Keep only the ones that are for bank_i and not already assigned
	while (r != NULL) {
		if (r->state == REQ_ASSIGNED) {
			r = r->next;
			continue;
		}

		uint8_t bank_index = (r->addr & BANK_MASK) >> 5;
		uint8_t row        = (r->addr & ROW_MASK) >> 16;
		if (bank_i == bank_index) {
			bank_req[nb_req] = r;
			nb_req++;
		}

		r = r->next;
	}

	if (nb_req == 0) return NULL;

	//1. Requests that are row buffer hits are prioritized over others
	for (size_t i = 0; i < nb_req; i++) {
		uint8_t row = (bank_req[i]->addr & ROW_MASK) >> 16;
		if (dram_rb_actions(bank_i, row) == RB_HIT) {
			row_buffer_hits[nb_hits] = r;
			nb_hits++;
		}
	}

	//2.Request that arrived earlier are prioritized over others
	//3. possibly, we have req from instr and mem issued at the same cycle
	if (nb_hits != 0) {
		Request *tmp = row_buffer_hits[0];
		for (size_t i = 1; i < nb_hits; i++) {
			if (row_buffer_hits[i]->cycle < tmp->cycle) {
				tmp = row_buffer_hits[i];
			} else if (row_buffer_hits[i]->cycle == tmp->cycle) {
				if (tmp->origin == INSTRUCTION) //mem has priority!
					tmp = row_buffer_hits[i];
			}
		}
		r_to_schedule = tmp;
	} else {
		Request *tmp = bank_req[0];
		for (size_t i = 1; i < nb_req; i++) {
			if (bank_req[i]->cycle < tmp->cycle) {
				tmp = bank_req[i];
			} else if (bank_req[i]->cycle == tmp->cycle) {
				if (tmp->origin == INSTRUCTION) //mem has priority!
					tmp = bank_req[i];
			}
		}
		r_to_schedule = tmp;
	}

	return r_to_schedule;
}

Row_buffer_states dram_rb_actions(uint8_t bank_index, uint32_t row) {
	if (dram.bank[bank_index].row_buffer == row)
		return RB_HIT;
	else if (dram.bank[bank_index].row_buffer == ROW_CLOSED)
		return RB_MISS;
	else
		return RB_CONFLICT;
}
