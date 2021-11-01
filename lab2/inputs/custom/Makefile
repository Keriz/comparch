AS = mips-linux-gnu-as
OBJCOPY = mips-linux-gnu-objcopy

INPUTS ?= $(wildcard *.s)

custom: $(patsubst %.s,%.x, $(INPUTS))

%.x: %.s
	$(AS) --mips32  $^ -o$(basename $^).o
	$(OBJCOPY) -O binary -j .text $(basename $^).o /dev/stdout | hexdump -v -e '4/1 "%02x" "\n"' > $@
	rm $(basename $^).o