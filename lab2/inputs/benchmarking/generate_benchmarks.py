import random
import shutil
import os


def gen_bm_1(name):
    itr = random.randint(10, 2000)
    f = open(name, "w")
    f.write(".text\n    lui $s0, 0x1000\n    lui $s1, 0x2000\n    addiu $s2, $0, " + hex(itr) +
            "\nloop:\n    lw $t0, 0($s0)\n    sw $t0, 0($s1)\n    addiu $s0, $s0, 0x4\n    addiu $s1, $s1, 0x4\n  \
                  addiu $s2, $s2, -1\n    nop\n    nop\n    bnez $s2, loop\n    addiu $v0, $0, 10\n    syscall\n")
    f.close()


def gen_bm_2(name):
    itr = random.randint(10, 2000)
    l_adds = [random.randint(0, itr) for i in range(itr)]
    s_adds = [random.randint(0, itr) for i in range(itr)]
    f = open(name, "w")
    f.write(".text\n    lui $s0, 0x1000\n    lui $s1, 0x3000\n")
    for l_add, s_add in zip(l_adds, s_adds):
        f.write("    addiu $s2, $s0, " + hex(4*l_add) + "\n")
        f.write("    lw $t0, 0($s2)\n")
        f.write("    addiu $s2, $s1, " + hex(4*s_add) + "\n")
        f.write("    sw $t0, 0($s2)\n")
    f.write("    addiu $v0, $0, 10\n    syscall\n")
    f.close()


bm1_dir = "bm1"
bm2_dir = "bm2"

# clean directories if tests are already generated
try:
    shutil.rmtree(bm1_dir)
    shutil.rmtree(bm2_dir)
except OSError as e:
    pass

os.mkdir(bm1_dir)
os.mkdir(bm2_dir)

for i in range(100):
    gen_bm_1(bm1_dir + "/test" + str(i) + ".s")
    gen_bm_2(bm2_dir + "/test" + str(i) + ".s")
