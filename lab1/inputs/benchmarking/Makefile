AS = mips-linux-gnu-as
OBJCOPY = mips-linux-gnu-objcopy

INPUT_BM1 ?= $(wildcard bm1/*.s)
INPUT_BM2 ?= $(wildcard bm2/*.s)
INPUT_BM3 ?= $(wildcard bm3/*.s)
INPUT_BM4 ?= $(wildcard bm4/*.s)
INPUT_BM5 ?= $(wildcard bm5/*.s)
INPUT_BM6 ?= $(wildcard bm6/*.s)

tests:
	python generate_benchmarks.py
	make assemble_tests

assemble_tests: as_bench1 as_bench2 as_bench3 as_bench4 as_bench5 as_bench6

as_bench1: $(patsubst %.s,%.x, $(INPUT_BM1))
as_bench2: $(patsubst %.s,%.x, $(INPUT_BM2))
as_bench3: $(patsubst %.s,%.x, $(INPUT_BM3))
as_bench4: $(patsubst %.s,%.x, $(INPUT_BM4))
as_bench5: $(patsubst %.s,%.x, $(INPUT_BM5))
as_bench6: $(patsubst %.s,%.x, $(INPUT_BM6))

%.x: %.s
	$(AS) --mips32  $^ -o$(basename $^).o
	$(OBJCOPY) -O binary -j .text $(basename $^).o /dev/stdout | hexdump -v -e '4/1 "%02x" "\n"' > $@
	rm $(basename $^).o

run_tests:
	python3 run_benchmarks.py
