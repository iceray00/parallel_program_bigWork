import matplotlib.pyplot as plt
import numpy as np

# 选择代表性的矩阵规模
matrix_sizes = [100, 500, 1000, 2000]

# 对于每个矩阵规模，获取OpenMP、Pthread和MPI的加速比和效率
# 这里以线程数=4, 进程数=4为例
openmp_speedup = [0.58, 2.6, 3.22, 2.3]
pthread_speedup = [0.51, 2.39, 3.16, 1.83]
mpi_speedup = [0.39, 3.25, 3.94, 1.66]

openmp_efficiency = [0.15, 0.6, 0.81, 0.58]
pthread_efficiency = [0.13, 0.6, 0.79, 0.46]
mpi_efficiency = [0.1, 0.81, 0.99, 0.42]

x = np.arange(len(matrix_sizes))  # 标签位置
width = 0.2  # 柱子的宽度

# 绘制加速比柱状图
fig, ax = plt.subplots(figsize=(10,6))
rects1 = ax.bar(x - width, openmp_speedup, width, label='OpenMP Speedup')
rects2 = ax.bar(x, pthread_speedup, width, label='Pthread Speedup')
rects3 = ax.bar(x + width, mpi_speedup, width, label='MPI Speedup')

# 添加标签和标题
ax.set_xlabel('Matrix Size')
ax.set_ylabel('Speedup')
ax.set_title('OpenMP vs Pthread vs MPI Speedup')
ax.set_xticks(x)
ax.set_xticklabels(matrix_sizes)
ax.legend()

# 添加数值标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig('speedup_matrix_comparison.pdf')
plt.show()

# 绘制效率柱状图
fig, ax = plt.subplots(figsize=(10,6))
rects1 = ax.bar(x - width, openmp_efficiency, width, label='OpenMP Efficiency')
rects2 = ax.bar(x, pthread_efficiency, width, label='Pthread Efficiency')
rects3 = ax.bar(x + width, mpi_efficiency, width, label='MPI Efficiency')

# 添加标签和标题
ax.set_xlabel('Matrix Size')
ax.set_ylabel('Efficiency')
ax.set_title('OpenMP vs Pthread vs MPI Efficiency')
ax.set_xticks(x)
ax.set_xticklabels(matrix_sizes)
ax.legend()

# 添加数值标签
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig('efficiency_matrix_comparison.pdf')
plt.show()
