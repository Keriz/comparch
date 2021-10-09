# Report Guillaume Thivolet - guillaume@glabs.ch

## Experiment setup, benchmark generation

I automated the benchmarking using python. Below is an explanation of all actions that are required to reproduce my work.

The `run_benchmarks.py` script has to be modified in order to change which parameter we are currently sweeping. Only the function being swept should be uncommented in the main function.

As the run_benchmarks.py program passes the argument being tested to the program, the c files also require some changes in order to accept this additional parameter.

There are listed just below. In `pipe.c`, the passed parameter from the console line argument should be used correctly in the cache initialization in relation to the parameter that we are testing.

`pipe.c, pipe_init()`

```c
void pipe_init(int param) {
	memset(&pipe, 0, sizeof(Pipe_State));
	pipe.PC = 0x00400000;

	instruction_cache = cache_init(1 << 13, 32, 4);
	data_cache        = cache_init(1 << 16, param, 8); testing block size
	//data_cache        = cache_init(1 << 16, 32, param); testing associativity
	//data_cache        = cache_init(1 << (10 + 31 - __builtin_clzl((uint32_t)param)), 32, 8); testing cache size
}
```


`shell.c, main`

```c
int main(int argc, char *argv[]) {

	/* Error Checking */
	if (argc < 2) {
		printf("Error: usage: %s <program_file_1> <program_file_2> ...\n",
		       argv[0]);
		exit(1);
	}

	printf("MIPS Simulator\n\n");

	initialize(strtol(argv[1], NULL, 10), argv[2], argc - 1);

	while (1)
		get_command();
}
```

`shell.c, initialize`

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

In `inputs/benchmarking/`, a Makefile is provided to generate the benchmarks object files and to subsequently run the automated tests on the simulator. The user must install the cross-compilation MIPS toolchain on his Linux first. I suggest to fetch it through the debian package manager:

```bash
sudo apt install binutils-mips-linux-gnu
```

__Possible usages are:__

- `make` to generate both benchmarks
- `make run_tests` to run the tests through the simulator

## Cache exploration by sweeping parameters

I was interested in optimizing the data cache regardless of the instruction cache. The instruction cache optimisation can also be done by writing specific benchmarks.

For instance, an instruction cache benchmark could be a program with multiple pointless functions containing a random number of `nop` instructions, and then randomly pointing out to other functions, until the end. This would force the instructions cache to flush and reload. We could also write a more sequential program with better space locality for the cache, which could be our second benchmark type.

Similarly for the data cache, we are going to write two benchmarks.

For each of those benchmarks, I generate 100 of them so that the benchmarking is less impacted by our program but rather gives an IPC that would be closer to reality.

For each parameter that I am testing, I ran both benchmarks' 100 programs generated and reported the average IPC in a bar chart. This will help in determining the sweet point of the curve.

__In retrospective, it probably would have lead to more interesting results to add more diversified benchmarks (more than two types), but designing tests is very time-consuming and I will leave it for another time (or lab).__

### Benchmark program 1

The first program streams the memory sequentially with an increment of 4 bytes on the address pointer between each access, and copies the accessed value in another array further in the memory.
The variant is in regard to the number of copies that we do (initial `addiu $s2, $0, 0xXXX` value). Below is an example program.

```asm
.text
    lui $s0, 0x1000
    lui $s1, 0x2000
    addiu $s2, $0, 0x4e9
loop:
    lw $t0, 0($s0)
    sw $t0, 0($s1)
    addiu $s0, $s0, 0x4
    addiu $s1, $s1, 0x4
    addiu $s2, $s2, -1
    nop
    nop
    bnez $s2, loop
    addiu $v0, $0, 10
    syscall
```

It's generation can be found in `inputs/benchmarking/generate_benchmarks.py`.

### Benchmark program 2

The second program generate `n` random accesses in the memory and copies the accessed value in another array.
The number of access is in the range of `[10;2000]`. Examples programs are longer than for the benchmark 1 as all the access are hard encoded and there's no loop. Below is an extract of a generated program.

```asm
.text
    lui $s0, 0x1000
    lui $s1, 0x3000
    addiu $s2, $s0, 0x3c
    lw $t0, 0($s2)
    addiu $s2, $s1, 0x80
    sw $t0, 0($s2)
    addiu $s2, $s0, 0xb8
    lw $t0, 0($s2)
    addiu $s2, $s1, 0x70
    sw $t0, 0($s2)
    addiu $s2, $s0, 0xe0
    lw $t0, 0($s2)
    .....
    addiu $v0, $0, 10
    syscall
```

It's generation can be found in `inputs/benchmarking/generate_benchmarks.py`.

### Block size

Example of execution in the terminal:

![Benchmark terminal](exemple_benchmark.png)
![Block size ](blocksize.png)

The other parameters were: 8-ways, 64KB Cache size.

The bigger the block size, the better the access performance for the sequential program (BM1), which is to be expected. Regarding BM2, which has a random access pattern, it is notable that after a certain block size it doesn't help much because the addresses are too far apart anyways.

An acceptable compromise would be **64 B or 128 B** for the block size, otherwise it just becomes too large to be actually implementable and is not reasonable.

### Cache size

![Cache size ](cachesize.png)

For a fixed 8-ways configuration, and 32B of block size, there is no improvement for a stream access to the array if the cache size increases. For the random access in BM2 it does help to a certain level, but shows no difference after 32KB.

The results shown here could probably be more relevant is the pattern access was different (with more written tests), and it would be easier to draw a conclusion from the plot.

For now, I would pick a cache of __64KB__.

### Number of sets (associativity)

![Associativity ](associativity.png)

If we increment the associativity (more tags can be stored per each way), the performance improvement stalls after 2-ways for BM2 and BM1. Having a 1-way would be equivalent as a direct-mapped cache, and too many ways would require additional logic (more area-consuming logic on the die as well as more combinational logic). I would stick to a number between __between 4 and 16__, depending on the cache level.

## Cache replacement policy exploration

TBD LATER (as of 08.10.2021).