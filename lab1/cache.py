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


sims = ["./lru", "./rr", "./fifo", "./mru"]

bold = "\033[1m"
green = "\033[0;32m"
red = "\033[0;31m"
normal = "\033[0m"


def compute_speedup(inputs):
    ipc = [[0 for i in range(len(inputs))] for o in range(4)]
    cycles = [[0 for i in range(len(inputs))] for o in range(4)]
    speedup = [[0 for i in range(len(inputs))] for o in range(4)]

    for i in inputs:
        if not os.path.exists(i):
            print(red + "ERROR -- input file (*.x) not found: " + i + normal)
            continue

        for s in sims:
            sim_out = run(s, i)
            sim_out = sim_out.split("\n")
            for so in zip(sim_out):
                s0, s1 = so[0].split(" ")
                if s0 == "IPC:":
                    ipc[sims.index(s)][inputs.index(i)] = float(s1)
                if s0 == "Cycles:":
                    cycles[sims.index(s)][inputs.index(i)] = float(s1)

    for i in range(0, len(sims)):
        for j in range(0, len(inputs)):
            #print(cycles[i][j], cycles[0][j])
            speedup[i][j] = round(float(cycles[0][j]/cycles[i][j]), 3)

    labels = [str(i).replace("inputs/", '').replace('.x', '') for i in inputs]

    x = np.arange(len(labels))  # the label locations
    width = 0.20  # the width of the bars

    fig, ax = plt.subplots()
    ax.set(ylim=(0, 5))
    rects1 = ax.bar(x - 1.5*width, speedup[0], width, label='LRU')
    rects2 = ax.bar(x - width/2, speedup[1], width, label='RR')
    rects3 = ax.bar(x + width/2, speedup[2], width, label='FIFO')
    rects4 = ax.bar(x + 1.5*width, speedup[3], width, label='MRU')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Speedup relative to LRU')
    ax.set_xlabel('Cache policy')
    ax.set_title('Speedup for LRU, RR, FIFO and MRU policies')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90, fontsize=7)
    ax.legend()

    size = 5
    ax.bar_label(rects1, padding=3, rotation='vertical', fontsize=size)
    ax.bar_label(rects2, padding=3, rotation='vertical', fontsize=size)
    ax.bar_label(rects3, padding=3, rotation='vertical', fontsize=size)
    ax.bar_label(rects4, padding=3, rotation='vertical', fontsize=size)

    fig.tight_layout()

    plt.savefig("policy.png", dpi=300)


def main():
    inputs = glob.glob("inputs/benchmarking/bm/*.x")
    inputs.extend(glob.glob("inputs/cache/*.x"))
    inputs.extend(glob.glob("inputs/long/*.x"))

    compute_speedup(inputs)
    # plot_cycles()


def run(si, i):
    global sim

    simproc = subprocess.Popen([si, i], executable=si, stdin=subprocess.PIPE,
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
