#!/bin/bash

POLICY=BLISS

case $POLICY in

    FCFS)

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FCFS_HLLL.stats ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FCFS_HHLL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FCFS_HHHL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FCFS_HHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FCFS_HHHHHHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace
    ;;

     FRFCFS)

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_HLLL.stats ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_HHLL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_HHHL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_HHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_HHHHHHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace
    ;;

    FRFCFS_Cap)

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_Cap_HLLL.stats ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_Cap_HHLL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_Cap_HHHL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_Cap_HHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  FRFCFS_Cap_HHHHHHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace
    ;;

    ATLAS)

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  ATLAS_HLLL.stats ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  ATLAS_HHLL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  ATLAS_HHHL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  ATLAS_HHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  ATLAS_HHHHHHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace

    ;;

    BLISS)

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  BLISS_HLLL.stats ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  BLISS_HHLL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  BLISS_HHHL.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/low-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  BLISS_HHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace

    ./ramulator configs/DDR4-config.cfg --mode=cpu --stats  BLISS_HHHHHHHH.stats ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace ./traces/high-mem-intensity.trace
    ;;

    esac