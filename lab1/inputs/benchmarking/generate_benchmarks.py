import random
import shutil
import os


def gen_bm_1(name):
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

    f.close()


def gen_bm_2(name):
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
