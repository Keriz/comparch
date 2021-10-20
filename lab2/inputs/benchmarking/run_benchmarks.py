#!/usr/bin/python

# Chris Fallin, 2012
# Yoongu Kim, 2013
# Juan Gomez Luna, 2017
# Minesh Patel, 2020

import os
import subprocess
import re
import glob
import matplotlib.pyplot as plt
import numpy as np


sim = "../../sim"

bold = "\033[1m"
green = "\033[0;32m"
red = "\033[0;31m"
normal = "\033[0m"


def block_size(bm1_inputs, bm2_inputs):

    block_sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    averages_b1 = []
    averages_b2 = []

    print(bold + "Testing block sizes" + normal)
    for bs in block_sizes:
        averages_b1.append(0)
        averages_b2.append(0)
        print(red + "   >Testing block size: " + str(bs) + normal)
        for i in bm1_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue
            sim_out = run(bs, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0, s1 = s[0].split(" ")
                if s0 == "IPC:":
                    averages_b1[block_sizes.index(bs)] += float(s1)
        for i in bm2_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue

            sim_out = run(bs, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0, s1 = s[0].split(" ")
                if s0 == "IPC:":
                    averages_b2[block_sizes.index(bs)] += float(s1)

    for i in range(0, len(block_sizes)):
        averages_b1[i] = round(averages_b1[i]/100, 3)
        averages_b2[i] = round(averages_b2[i]/100, 3)

    print("  " + bold + "Stats (avg over 100 tests)".ljust(14) +
          "BM1".center(25) + "BM2".center(25) + normal)

    for bs in block_sizes:
        i = block_sizes.index(bs)
        print("  " + bold + ("IPC @ BS " + str(bs) + " KB").ljust(25) +
              str(averages_b1[i]).center(25) + str(averages_b2[i]).center(25) + normal)

    print("  " + green + "BLOCK SIZE TEST COMPLETED" + normal)

    labels = [str(i) for i in block_sizes]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, averages_b1, width, label='Benchmark 1')
    rects2 = ax.bar(x + width/2, averages_b2, width, label='Benchmark 2')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average IPC (over 100 benchmark programs)')
    ax.set_xlabel('Block size (B)')
    ax.set_title('IPC in relation to the cache block size')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig("blocksize.png")


def cache_size(bm1_inputs, bm2_inputs):
    cache_sizes = [1, 2, 4, 8, 16, 32, 64, 128]
    averages_b1 = []
    averages_b2 = []

    print(bold + "Testing cache sizes" + normal)
    for cs in cache_sizes:
        averages_b1.append(0)
        averages_b2.append(0)
        print(red + "   >Testing cache size: " + str(cs) + normal)
        for i in bm1_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue
            sim_out = run(cs, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0, s1 = s[0].split(" ")
                if s0 == "IPC:":
                    averages_b1[cache_sizes.index(cs)] += float(s1)
        for i in bm2_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue

            sim_out = run(cs, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0, s1 = s[0].split(" ")
                if s0 == "IPC:":
                    averages_b2[cache_sizes.index(cs)] += float(s1)

    for i in range(0, len(cache_sizes)):
        averages_b1[i] = round(averages_b1[i]/100, 3)
        averages_b2[i] = round(averages_b2[i]/100, 3)

    print("  " + bold + "Stats (avg over 100 tests)".ljust(14) +
          "BM1".center(25) + "BM2".center(25) + normal)

    for cs in cache_sizes:
        i = cache_sizes.index(cs)
        print("  " + bold + ("IPC @ CS  " + str(cs) + " KB").ljust(25) +
              str(averages_b1[i]).center(25) + str(averages_b2[i]).center(25) + normal)

    print("  " + green + "CACHE SIZE TEST COMPLETED" + normal)

    labels = [str(i) for i in cache_sizes]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, averages_b1, width, label='Benchmark 1')
    rects2 = ax.bar(x + width/2, averages_b2, width, label='Benchmark 2')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average IPC (over 100 benchmark programs)')
    ax.set_xlabel('Cache size (KB)')
    ax.set_title('IPC in relation to the cache size')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig("cachesize.png")


def associativity(bm1_inputs, bm2_inputs):
    asso = [1, 2, 4, 8, 16, 32, 64, 128]
    averages_b1 = []
    averages_b2 = []

    print(bold + "Testing associativity sizes" + normal)
    for a in asso:
        averages_b1.append(0)
        averages_b2.append(0)
        print(red + "   >Testing associativity size: " + str(a) + normal)
        for i in bm1_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue
            sim_out = run(a, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0, s1 = s[0].split(" ")
                if s0 == "IPC:":
                    averages_b1[asso.index(a)] += float(s1)
        for i in bm2_inputs:
            if not os.path.exists(i):
                print(red + "ERROR -- input file (*.x) not found: " + i + normal)
                continue

            sim_out = run(a, i)

            sim_out = sim_out.split("\n")

            for s in zip(sim_out):
                s0, s1 = s[0].split(" ")
                if s0 == "IPC:":
                    averages_b2[asso.index(a)] += float(s1)

    for i in range(0, len(asso)):
        averages_b1[i] = round(averages_b1[i]/100, 3)
        averages_b2[i] = round(averages_b2[i]/100, 3)

    print("  " + bold + "Stats (avg over 100 tests)".ljust(14) +
          "BM1".center(25) + "BM2".center(25) + normal)

    for a in asso:
        i = asso.index(a)
        print("  " + bold + ("IPC @ " + str(a) + "ways").ljust(25) +
              str(averages_b1[i]).center(25) + str(averages_b2[i]).center(25) + normal)

    print("  " + green + "ASSOCIATIVITY TEST COMPLETED" + normal)

    labels = [str(i) for i in asso]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, averages_b1, width, label='Benchmark 1')
    rects2 = ax.bar(x + width/2, averages_b2, width, label='Benchmark 2')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average IPC (over 100 benchmark programs)')
    ax.set_xlabel('Associativity')
    ax.set_title('IPC in relation to the number of ways')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig("associativity.png")


def main():
    bm1_inputs = glob.glob("bm1/*.x")
    bm2_inputs = glob.glob("bm2/*.x")

    block_size(bm1_inputs, bm2_inputs)
    #cache_size(bm1_inputs, bm2_inputs)
    #associativity(bm1_inputs, bm2_inputs)


def run(arg, i):
    global sim

    simproc = subprocess.Popen([sim, str(arg), i], executable=sim, stdin=subprocess.PIPE,
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
