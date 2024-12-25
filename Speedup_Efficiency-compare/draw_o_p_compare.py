import matplotlib.pyplot as plt
import numpy as np

# 数据准备
threads = [2, 4, 8, 16]

# OpenMP 加速比
openmp_speedup = [3.87, 4.41, 3.58, 2.52]
# Pthread 加速比
pthread_speedup = [0.7, 0.43, 0.27, 0.17]

# OpenMP 效率
openmp_efficiency = [1.93, 1.1, 0.45, 0.16]
# Pthread 效率
pthread_efficiency = [0.35, 0.11, 0.03, 0.01]

# 绘制加速比对比图
plt.figure(figsize=(10, 6))
plt.plot(threads, openmp_speedup, marker='o', label='OpenMP Speedup')
plt.plot(threads, pthread_speedup, marker='s', label='Pthread Speedup')
plt.xlabel('thread')
plt.ylabel('Speedup')
plt.title('OpenMP vs Pthread Speedup')
plt.legend()
plt.grid(True)
plt.xticks(threads)
plt.savefig('speedup_comparison.pdf')
plt.show()

# 绘制效率对比图
plt.figure(figsize=(10, 6))
plt.plot(threads, openmp_efficiency, marker='o', label='OpenMP Efficiency')
plt.plot(threads, pthread_efficiency, marker='s', label='Pthread Efficiency')
plt.xlabel('thread')
plt.ylabel('Efficiency')
plt.title('OpenMP vs Pthread Efficiency')
plt.legend()
plt.grid(True)
plt.xticks(threads)
plt.savefig('efficiency_comparison.pdf')
plt.show()
