#!/bin/bash

# 定义矩阵规模数组和进程数数组
matrix_sizes=(10 50 100 200 300 500 700 1000 1300 1600 2000 2500)
process_counts=(1 2 4 6)

# 可执行文件路径
program="./mpi"

# 遍历矩阵规模和进程数组合
for size in "${matrix_sizes[@]}"; do
    for procs in "${process_counts[@]}"; do
        mpirun -np $procs $program $size
    done
done
