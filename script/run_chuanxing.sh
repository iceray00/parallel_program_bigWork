#!/bin/bash

# 定义矩阵大小的数组
matrix_sizes=(10 50 100 200 300 500 700 1000 1300 1600 2000 2500)

# 可执行文件路径
program="./chuanxing"

# 检查程序是否存在
if [ ! -f "$program" ]; then
    echo "错误: 未找到可执行文件 $program，请确保已编译程序。"
    exit 1
fi

# 遍历数组中的矩阵大小并运行程序
for size in "${matrix_sizes[@]}"; do
#    echo "矩阵大小: $size"
    $program $size
    if [ $? -ne 0 ]; then
        echo "错误: 程序在矩阵大小 $size 时运行失败。"
        exit 1
    fi
#    echo "========================================="
done

echo "所有矩阵大小运行完成！"
