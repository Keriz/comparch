AS = mips-linux-gnu-as
OBJCOPY = mips-linux-gnu-objcopy

INPUT_BM1 ?= $(wildcard bm1/*.s)
INPUT_BM2 ?= $(wildcard bm2/*.s)

tests:
	python generate_benchmarks.py
	make assemble_tests

assemble_tests: as_bench1 as_bench2

as_bench1: $(patsubst %.s,%.x, $(INPUT_BM1))
as_bench2: $(patsubst %.s,%.x, $(INPUT_BM2))

%.x: %.s
	$(AS) --mips32  $^ -o$(basename $^).o
	$(OBJCOPY) -O binary -j .text $(basename $^).o /dev/stdout | hexdump -v -e '4/1 "%02x" "\n"' > $@
	rm $(basename $^).o

run_tests:
	python run_benchmarks.py
