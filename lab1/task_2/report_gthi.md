# Report Guillaume Thivolet

## Experiment setup, benchmark generation

I have automated the benchmarking using python. Below is an explanation of all actions that are required to reproduce my work.

The `run_benchmarks.py` script has to be modified in order to change which parameter we are currently sweeping. Only the function being sweeped should be uncommomented in the main. Accordingly, in `pipe.c`, the changed parameter should be placed accordingly in the cache initialization.

pipe.c, pipe_init()

```c
void pipe_init(int param) {
	memset(&pipe, 0, sizeof(Pipe_State));
	pipe.PC = 0x00400000;

	instruction_cache = cache_init(1 << 13, 32, 4);
	data_cache        = cache_init(1 << 16, param, 8);
}
```

As the run_benchmarks.py program passes the argument being tested to the program, the c files also require some changes in order to accept this additional parameter.

There are listed just below.

shell.c, new main

```c
int main(int argc, char *argv[]) {

	/* Error Checking */
	if (argc < 2) {
		printf("Error: usage: %s <program_file_1> <program_file_2> ...\n",
		       argv[0]);
		exit(1);
	}

	printf("MIPS Simulator\n\n");

	initialize(strtol(argv[1], NULL, 10), argv[2], argc - 2);

	while (1)
		get_command();
}
```

shell.c, new initialize

```c
void initialize(int param, char *program_filename, int num_prog_files) {
	int i;

	init_memory();

	pipe_init(param);
	for (i = 1; i < num_prog_files; i++) {
		load_program(program_filename);
		while (*program_filename++ != '\0')
			;
	}

	RUN_BIT = TRUE;
}
```

pipe.c, new pipe_init

```c
void pipe_init(int param) {
	memset(&pipe, 0, sizeof(Pipe_State));
	pipe.PC = 0x00400000;

	instruction_cache = cache_init(1 << 13, 32, 4);
	data_cache        = cache_init(1 << 16, param, 8);
}
```

In `inputs/benchmarking/`, a Makefile is provided to generate the benchmarks object files and to subsequently run the automated tests on the simulator. The user must install the cross-compilation MIPS toolchain on his Linux first. I suggest to fetch it through the debian package manager:

```bash
sudo apt install binutils-mips-linux-gnu
```

Possible usages are:

- `make` to generate both benchmarks
- `make run_tests` to run the tests through the simulator

## Cache exploration by sweeping parameters

I was interested in optimizing the data cache regardless of the instruction cache. The instruction cache optimisation can also be done by writing specific benchmarks.

For instance, an instruction cache benchmark could be a program with multiple pointless functions containing a random number of `nop` instructions, and then randomly pointing out to other functions, until the end. This would force the insrtuction cache to flush and reload. We could also write a more sequential program with better space locality for the cache, which could be our second benchmark type.

Similarly for the data cache, we are going to write two benchmarks.

For each of those benchmarks, I generate 100 of them so that the benchmarking is less impacted by our program but rather gives an IPC that would be closer to reality.

For each parameter that I am testing, I ran both benkmarks' 100 programs generated and reported the average IPC in a bar chart. This will help in determining the sweet point of the curve.

### Benchmark program 1

The first program streams the memory sequentially with an increment of 4 bytes on the address pointer between each access, and copy the accessed value in another array.

It's generation can be found in `inputs/benchmarking/generate_benchmarks.py`.

### Benchmark program 2

The second program generate 500 random accesses in the memory and copies the accessed value in another array.

It's generation can be found in `inputs/benchmarking/generate_benchmarks.py`.

### Block size

### Cache size

### Number of sets (associativity)

## Cache replacement policy exploration
