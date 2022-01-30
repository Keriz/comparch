import random
import shutil
import os

# block size, 8-ways 64kB cache


def gen_bm_1(name):
    itr = random.randint(100, 3000)
    f = open(name, "w")
    f.write(".text\n    lui $s0, 0x1000\n    lui $s1, 0x2000\n    addiu $s2, $0, " + hex(itr) +
            "\nloop:\n    lw $t0, 0($s0)\n    sw $t0, 0($s1)\n    addiu $s0, $s0, 0x4\n    addiu $s1, $s1, 0x4\n  \
                  addiu $s2, $s2, -1\n    nop\n    nop\n    bnez $s2, loop\n    addiu $v0, $0, 10\n    syscall\n")
    f.close()


# associativity 32B blocks 64kB cache
def gen_bm_2(name):
    itr = random.randint(10, 2000)
    l_adds = [random.randint(0, itr) for i in range(itr)]
    s_adds = [random.randint(0, itr) for i in range(itr)]
    f = open(name, "w")
    f.write(".text\n    lui $s0, 0x1000\n    lui $s1, 0x3000\n")
    for l_add, s_add in zip(l_adds, s_adds):
        f.write("    addiu $s2, $s0" +
                hex(4*l_add) + "\n")
        f.write("    lw $t0, 0($s2)\n")
        f.write("    addiu $s2, $s1" +
                hex(4*s_add) + "\n")
        f.write("    sw $t0, 0($s2)\n")
    f.write("    addiu $v0, $0, 10\n    syscall\n")
    f.close()

# cache policy


def gen_bm_3(name):
    itr = 100
    f = open(name, "w")
    f.write(".text\n    lui $s0, 0x1000\n")
    for i in range(itr):
        samples = random.sample(range(1, 12), 8)
        for s in samples:
            f.write("    lui $s1, " +
                    hex(s % 8) + "\n")
            f.write("    addu $s2, $s1, $s0" + "\n")
            f.write("    lw $t0, 0($s2)\n")
    f.write("    addiu $v0, $0, 10\n    syscall\n")
    f.close()


def gen_bm_4(name):
    itr = 500
    f = open(name, "w")
    f.write(".text\n    lui $s0, 0x1000\n")
    samples = random.sample(range(0, 8), 8)
    for i in range(itr):
        for s in samples:
            f.write("    lui $s1, " +
                    hex(s % 8) + "\n")
            f.write("    addu $s2, $s1, $s0" + "\n")
            f.write("    lw $t0, 0($s2)\n")
    f.write("    addiu $v0, $0, 10\n    syscall\n")
    f.close()


def gen_bm_5(name):
    fn_order = [i + 1 for i in range(9)]
    random.shuffle(fn_order)

    fn_length = [random.randint(20, 400) for i in range(10)]

    f = open(name, "w")

    f.write(".text\n")

    for i in range(10):
        f.write("fn_" + str(i) + ":\n")
        for j in range(fn_length[i]):
            f.write("    nop\n")
        if i != 9:
            f.write("    beqz $0, fn_" + str(fn_order[i]) + "\n")
        else:
            f.write("    addiu $v0, $0, 10\n    syscall\n")


def gen_bm_6(name):
    fn_decrement = [random.randint(-4, -1) for i in range(4)]
    fn_length = [random.randint(20, 400) for i in range(4)]
    fn_distance = [random.randint(20, 1000) for i in range(4)]

    f = open(name, "w")
    f.write(".text\n    addiu $t0, $0, 100\n    addiu $t1, $0, 1\n    addiu $t2, $0, 2\n    addiu $t3, $0, 3\nfn_main:\n    and $t4, $t0, $t3\n    nop\n    nop\n    blez $t0, end\n    nop\n    nop\n    beq $t4, $0, fn_0\n    nop\n    nop\n    beq $t4, $t1, fn_1\n    nop\n    nop\n    beq $t4, $t2, fn_2\n    nop\n    nop\n    beq $t4, $t3, fn_3\nend:\n    addiu $v0, $0, 10\n    syscall\n")
    for i in range(4):
        for j in range(fn_distance[i]):
            f.write("    nop\n")
        f.write("fn_" + str(i) + ":\n")
        f.write("    addi $t0, $t0, " + str(fn_decrement[i]) + "\n")
        for j in range(fn_length[i]):
            f.write("    nop\n")
        f.write("    beqz $0, fn_main\n")
    f.close()


bm1_dir = "bm1"
bm2_dir = "bm2"
bm3_dir = "bm3"
bm4_dir = "bm4"
bm5_dir = "bm5"
bm6_dir = "bm6"

# clean directories if tests are already generated
try:
    shutil.rmtree(bm1_dir)
    shutil.rmtree(bm2_dir)
    shutil.rmtree(bm3_dir)
    shutil.rmtree(bm4_dir)
    shutil.rmtree(bm5_dir)
    shutil.rmtree(bm6_dir)
except OSError as e:
    pass

os.mkdir(bm1_dir)
os.mkdir(bm2_dir)
os.mkdir(bm3_dir)
os.mkdir(bm4_dir)
os.mkdir(bm5_dir)
os.mkdir(bm6_dir)

for i in range(100):
    gen_bm_1(bm1_dir + "/test" + str(i) + ".s")
    gen_bm_2(bm2_dir + "/test" + str(i) + ".s")
    gen_bm_3(bm3_dir + "/test" + str(i) + ".s")

""" for i in range(3):
    gen_bm_4(bm4_dir + "/test" + str(i) + ".s")

 """
""" for i in range(100):
    gen_bm_5(bm5_dir + "/test" + str(i) + ".s")
    gen_bm_6(bm6_dir + "/test" + str(i) + ".s")
 """
