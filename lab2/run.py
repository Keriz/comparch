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

ref = "basesim.exe"
sim = "sim.exe"

bold = "\033[1m"
green = "\033[0;32m"
red = "\033[0;31m"
normal = "\033[0m"


def main():
    all_inputs = glob.glob("inputs/*/*.x")

    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="*", default=all_inputs)
    parser = parser.parse_args()

    for i in parser.inputs:
        if not os.path.exists(i):
            print(red + "ERROR -- input file (*.x) not found: " + i + normal)
            continue

        print(bold + "Testing: " + normal + i)
        ref_out, sim_out = run(i)

        print("  " + "Stats".ljust(14) +
              "BaselineSim".center(14) + "YourSim".center(14))

        ref_out = ref_out.split("\n")
        sim_out = sim_out.split("\n")

        nocheck = 0
        error = 0
        for r, s in zip(ref_out, sim_out):

            r0 = r.split()[0]
            r1 = r.split()[1]
            s1 = s.split()[1]

            print("  " + r0.ljust(14) + r1.center(14) + s1.center(14),)

            if (r0 == "Cycles:"):
                nocheck = 1
            if (r1 != s1 and nocheck == 0):
                print("  " + red + "ERROR" + normal)
                error = 1
        else:
            print()

        if error == 0:
            print("  " + green + "REGISTER CONTENTS OK" + normal)
        print()


def run(i):
    global ref, sim

    refproc = subprocess.Popen([ref, i], executable=ref, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    simproc = subprocess.Popen([sim, i], executable=sim, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    cmds = b""
    cmdfile = os.path.splitext(i)[0] + ".cmd"
    if os.path.exists(cmdfile):
        cmds += open(cmdfile).read().encode('utf-8')

    cmds += b"\ngo\nrdump\nquit\n"
    (r, r_err) = refproc.communicate(input=cmds)
    (s, s_err) = simproc.communicate(input=cmds)

    return filter_stats(r.decode('utf-8')), filter_stats(s.decode('utf-8'))


def filter_stats(out):
    lines = out.split("\n")
    regex = re.compile(
        "^(HI:)|(LO:)|(R\d+:)|(PC:)|(Cycles:)|(Fetched\w+:)|(Retired\w+:)|(IPC:)|(Flushes:).*$")
    out = []
    for l in lines:
        if regex.match(l):
            out.append(l)

    return "\n".join(out)


if __name__ == "__main__":
    main()
