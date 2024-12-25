#!/bin/bash

# 定义矩阵大小和线程数的数组
matrix_sizes=(10 50 100 200 300 500 700 1000 1300 1600 2000 2500)
thread_counts=(1 2 4 8 16)

# 可执行文件路径
program="./pthread"

# 检查程序是否存在
if [ ! -f "$program" ]; then
    echo "错误: 未找到可执行文件 $program，请先编译程序。"
    exit 1
fi

# 遍历矩阵大小和线程数
for size in "${matrix_sizes[@]}"; do
    for threads in "${thread_counts[@]}"; do
#        echo "矩阵大小为: $size | 线程数为: $threads"
        $program $size $threads
        if [ $? -ne 0 ]; then
            echo "错误: 程序在矩阵大小 $size 和线程数 $threads 时运行失败。"
            exit 1
        fi
#        echo "----------------------------------------"
    done
done

echo "所有测试运行完成！"
