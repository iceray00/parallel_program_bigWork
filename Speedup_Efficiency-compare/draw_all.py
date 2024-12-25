import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 选择的矩阵规模
matrix_sizes = [10, 100, 500, 1000, 2500]
threads = [2, 4, 8, 16]

# OpenMP 数据
openmp_speedup = {
    10: [3.87, 4.41, 3.58, 2.52],
    100: [0.91, 0.83, 0.53, 0.28],
    500: [1.86, 2.60, 2.71, 2.16],
    1000: [1.91, 3.22, 2.30, 1.90],
    2500: [1.90, 2.20, 1.95, 2.06]
}

openmp_efficiency = {
    10: [1.93, 1.10, 0.45, 0.16],
    100: [0.46, 0.21, 0.07, 0.02],
    500: [0.93, 0.65, 0.34, 0.13],
    1000: [0.96, 0.81, 0.29, 0.12],
    2500: [0.95, 0.55, 0.24, 0.13]
}

# Pthread 数据
pthread_speedup = {
    10: [0.70, 0.43, 0.27, 0.17],
    100: [0.81, 0.56, 0.33, 0.18],
    500: [1.86, 2.39, 2.02, 1.46],
    1000: [1.90, 3.16, 2.83, 2.81],
    2500: [1.92, 1.73, 1.82, 1.79]
}

pthread_efficiency = {
    10: [0.35, 0.11, 0.03, 0.01],
    100: [0.41, 0.14, 0.04, 0.011],
    500: [0.93, 0.60, 0.25, 0.09],
    1000: [0.95, 0.79, 0.35, 0.18],
    2500: [0.96, 0.43, 0.23, 0.11]
}

# 创建DataFrame
data = []
for size in matrix_sizes:
    for idx, thread in enumerate(threads):
        data.append({
            '矩阵规模': size,
            '线程数': thread,
            '加速比_OpenMP': openmp_speedup[size][idx],
            '效率_OpenMP': openmp_efficiency[size][idx],
            '加速比_Pthread': pthread_speedup[size][idx],
            '效率_Pthread': pthread_efficiency[size][idx]
        })

df = pd.DataFrame(data)


# 设置绘图风格
sns.set(style="whitegrid")

# 创建子图
fig, axes = plt.subplots(3, 2, figsize=(15, 18))
fig.suptitle('OpenMP vs Pthread Speedup', fontsize=16)

# 定义颜色和标记
colors = {'OpenMP': 'blue', 'Pthread': 'green'}
markers = {'OpenMP': 'o', 'Pthread': 's'}

# 绘制加速比
for i, size in enumerate(matrix_sizes):
    ax = axes[i//2, i%2]
    subset = df[df['矩阵规模'] == size]
    ax.plot(subset['线程数'], subset['加速比_OpenMP'], marker='o', color='blue', label='OpenMP 加速比')
    ax.plot(subset['线程数'], subset['加速比_Pthread'], marker='s', color='green', label='Pthread 加速比')
    ax.set_title(f'矩阵规模 = {size}')
    ax.set_xlabel('线程数')
    ax.set_ylabel('加速比 (Speedup)')
    ax.legend()
    ax.grid(True)
    ax.set_xticks(threads)

# 移除空白子图
for j in range(len(matrix_sizes), 3*2):
    fig.delaxes(axes.flatten()[j])

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('speedup_comparison_multiple_matrix_sizes.png')
plt.show()


# 创建子图
fig, axes = plt.subplots(3, 2, figsize=(15, 18))
fig.suptitle('OpenMP vs Pthread Efficiency', fontsize=16)

# 绘制效率
for i, size in enumerate(matrix_sizes):
    ax = axes[i//2, i%2]
    subset = df[df['矩阵规模'] == size]
    ax.plot(subset['线程数'], subset['效率_OpenMP'], marker='o', color='blue', label='OpenMP Efficiency')
    ax.plot(subset['线程数'], subset['效率_Pthread'], marker='s', color='green', label='Pthread Efficiency')
    ax.set_title(f'Matrix Size = {size}')
    ax.set_xlabel('Threads')
    ax.set_ylabel('Efficiency')
    ax.legend()
    ax.grid(True)
    ax.set_xticks(threads)

# 移除空白子图
for j in range(len(matrix_sizes), 3*2):
    fig.delaxes(axes.flatten()[j])

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('efficiency_comparison_multiple_matrix_sizes.png')
plt.show()








# 计算平均加速比和效率（可选，根据需求调整）
# 这里我们选择不计算平均，而是展示每个矩阵规模的趋势

# 绘制所有矩阵规模的加速比
plt.figure(figsize=(12, 8))
for size in matrix_sizes:
    subset = df[df['矩阵规模'] == size]
    plt.plot(subset['线程数'], subset['加速比_OpenMP'], marker='o', label=f'OpenMP S, size={size}')
    plt.plot(subset['线程数'], subset['加速比_Pthread'], marker='s', linestyle='--', label=f'Pthread S, size={size}')

plt.xlabel('Threads')
plt.ylabel('Speedup')
plt.title('OpenMP vs Pthread Speedup in All Matrix Sizes')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(threads)
plt.tight_layout()
plt.savefig('speedup_trends_all_matrix_sizes.png')
plt.show()

# 绘制所有矩阵规模的效率
plt.figure(figsize=(12, 8))
for size in matrix_sizes:
    subset = df[df['矩阵规模'] == size]
    plt.plot(subset['线程数'], subset['效率_OpenMP'], marker='o', label=f'OpenMP E, size={size}')
    plt.plot(subset['线程数'], subset['效率_Pthread'], marker='s', linestyle='--', label=f'Pthread E, size={size}')

plt.xlabel('Threads')
plt.ylabel('Efficiency')
plt.title('OpenMP vs Pthread Efficiency in All Matrix Sizes')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(threads)
plt.tight_layout()
plt.savefig('efficiency_trends_all_matrix_sizes.png')
plt.show()







# 选择的矩阵规模
selected_sizes = [10, 100, 500, 1000, 2500]

# 创建子图
fig, axes = plt.subplots(len(selected_sizes), 1, figsize=(12, 5*len(selected_sizes)))
fig.suptitle('OpenMP vs Pthread Speedup in Selected Matrix Sizes', fontsize=16)

for i, size in enumerate(selected_sizes):
    ax = axes[i]
    subset = df[df['矩阵规模'] == size]
    x = np.arange(len(threads))
    width = 0.35  # 柱子的宽度

    ax.bar(x - width/2, subset['加速比_OpenMP'], width, label='OpenMP Speedup', color='blue')
    ax.bar(x + width/2, subset['加速比_Pthread'], width, label='Pthread Speedup', color='green')

    ax.set_xlabel('Threads')
    ax.set_ylabel('Speedup')
    ax.set_title(f'Matrix Size = {size}')
    ax.set_xticks(x)
    ax.set_xticklabels(threads)
    ax.legend()
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('speedup_bar_multiple_matrix_sizes.png')
plt.show()




# 创建子图
fig, axes = plt.subplots(len(selected_sizes), 1, figsize=(12, 5*len(selected_sizes)))
fig.suptitle('OpenMP vs Pthread Efficiency in Selected Matrix Sizes', fontsize=16)

for i, size in enumerate(selected_sizes):
    ax = axes[i]
    subset = df[df['矩阵规模'] == size]
    x = np.arange(len(threads))
    width = 0.35  # 柱子的宽度

    ax.bar(x - width/2, subset['效率_OpenMP'], width, label='OpenMP Efficiency', color='blue')
    ax.bar(x + width/2, subset['效率_Pthread'], width, label='Pthread Efficiency', color='green')

    ax.set_xlabel('Threads')
    ax.set_ylabel('Efficiency')
    ax.set_title(f'Matrix Size = {size}')
    ax.set_xticks(x)
    ax.set_xticklabels(threads)
    ax.legend()
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('efficiency_bar_multiple_matrix_sizes.png')
plt.show()

