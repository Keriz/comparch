#!/usr/bin/python

# Chris Fallin, 2012
# Yoongu Kim, 2013
# Juan Gomez Luna, 2017
# Minesh Patel, 2020

import sys
import os
import subprocess
import re
import glob
import argparse

sim = "./sim"

bold = "\033[1m"
green = "\033[0;32m"
red = "\033[0;31m"
normal = "\033[0m"


def block_size(bm1_inputs, bm2_inputs):

    block_sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    averages_b1 = []
    averages_b2 = []

    print(red + "Testing block size" + normal + i)
    for bs in block_sizes:
        for i in bm1_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue

            sim_out = run(bs, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0 = s.split()[0]
                s1 = s.split()[1]

                if s0 == "IPC :":
                    averages_b1[block_sizes.index(bs)] += s1
        for i in bm2_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue

            sim_out = run(bs, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0 = s.split()[0]
                s1 = s.split()[1]

                if s0 == "IPC :":
                    averages_b2[block_sizes.index(bs)] += s1

    for i in range(0, len(block_sizes)):
        averages_b1[i] /= 100
        averages_b2[i] /= 100

    print("  " + bold + "Stats (avg over 100 tests)".ljust(14) +
          "BM1".center(14) + "BM2".center(14) + normal)

    for bs in block_sizes:
        i = block_sizes.index(bs)
        print("  " + bold + ("IPC @ BS " + str(bs)).ljust(14) +
              averages_b1[i].center(14) + averages_b2[i].center(14) + normal)

    print("  " + green + "BLOCK SIZE TEST COMPLETED" + normal)


def cache_size(all_inputs):
    a = 0


def associativity(all_inputs):
    a = 0


def generate_test1(all_inputs):
    a = 0


def generate_test2(all_inputs):
    a = 0


def main():
    bm1_inputs = glob.glob("inputs/benchmarking/bm1/*.x")
    bm2_inputs = glob.glob("inputs/benchmarking/bm2/*.x")

    block_size(bm1_inputs, bm2_inputs)


def run(arg, i):
    global sim

    simproc = subprocess.Popen([sim, arg, i], executable=sim, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    cmds = b""
    cmdfile = os.path.splitext(i)[0] + ".cmd"
    if os.path.exists(cmdfile):
        cmds += open(cmdfile).read().encode('utf-8')

    cmds += b"\ngo\nrdump\nquit\n"
    (s, s_err) = simproc.communicate(input=cmds)

    return filter_stats(s.decode('utf-8'))


def filter_stats(out):
    lines = out.split("\n")
    regex = re.compile(
        "^(Cycles:)|(IPC:)|(Flushes:).*$")
    out = []
    for l in lines:
        if regex.match(l):
            out.append(l)

    return "\n".join(out)


if __name__ == "__main__":
    main()
