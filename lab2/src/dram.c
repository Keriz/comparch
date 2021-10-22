#include "dram.h"

Dram dram;

void dram_initialize() {
	for (size_t i = 0; i < NB_BANKS; i++) {
		memset(dram.banks[i].rows, 0, sizeof(Row) * NB_ROWS);
		memset(dram.banks[i].row_buffer, 0, sizeof(Row));
	}

	//initialize mem controller
	req_queue       = malloc(sizeof(Request));
	req_queue->next = NULL;
	req_queue->prev = NULL;
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
}

void dram_mc_issue_request() {
}

void remove_req(Request *r) {
	if (!r) exit(3);

	if (r->prev != NULL)
		r->prev->next = r->next;
	free(r);
}

void add_req(Request *r) {
	if (!r) exit(3);
	Request *new_r = malloc(sizeof(Request));
	if (!new_r) exit(3);

	new_r->prev = queue_get_last();
	new_r->next = NULL;
}

Request *queue_get_last() {
	Request *r = req_queue;
	while (r->next != NULL)
		r = r->next;
	return r;
}

/*
*/
void dram_mc_scan_queue() {
	//only one req scheudable? issue a dram_access

	//multiple req scheludable? find which one to issue according to fr_fcfs policy
}

void dram_access() {
	dram.cmd_bus.counter     = 4;
	dram.address_bus.counter = 4;
}

/*
1. Requests that are row buffer hits are prioritized over others
2. Requests that arrived earlier are prioritized over others
3. Requests coming from the memory stage are priorized over others
*/
/* void fr_fcfs_policy(Request_queue *rq) {
	Request r_scheduled;
	Request *r = rq->first;

	while (r != NULL) {

		r = r->next;
	}
} */