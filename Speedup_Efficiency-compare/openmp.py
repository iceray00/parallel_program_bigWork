import matplotlib.pyplot as plt

# 数据
matrix_sizes = [10, 50, 100, 200, 300, 500, 700, 1000, 1300, 1600, 2000, 2500]
speedup = {
    2: [3.87, 0.74, 0.91, 1.43, 1.61, 1.86, 2.11, 1.91, 1.9, 1.88, 1.92, 1.9],
    4: [4.41, 0.58, 0.83, 1.87, 2.49, 2.6, 3.82, 3.22, 2.32, 2.55, 2.3, 2.2],
    8: [3.58, 0.3, 0.53, 1.26, 1.9, 2.71, 3.46, 2.3, 1.76, 1.89, 1.94, 1.95],
    16: [2.52, 0.17, 0.28, 0.76, 1.2, 2.16, 1.46, 1.9, 1.64, 2.11, 2.02, 2.06]
}
efficiency = {
    2: [1.93, 0.37, 0.46, 0.72, 0.8, 0.93, 1.06, 0.96, 0.95, 0.94, 0.96, 0.95],
    4: [1.1, 0.15, 0.21, 0.47, 0.62, 0.65, 0.96, 0.81, 0.58, 0.64, 0.58, 0.55],
    8: [0.45, 0.04, 0.07, 0.16, 0.24, 0.34, 0.43, 0.29, 0.22, 0.24, 0.24, 0.24],
    16: [0.16, 0.01, 0.02, 0.05, 0.08, 0.13, 0.09, 0.12, 0.1, 0.13, 0.13, 0.13]
}

# 绘制加速比图
plt.figure(figsize=(12, 6))
for t, values in speedup.items():
    plt.plot(matrix_sizes, values, marker='o', label=f't={t}')
plt.title('Speedup -- Matrix Size', fontsize=14)
plt.xlabel('Matrix Size', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig('speedup_openmp.pdf')
# 显示加速比图
plt.show()

# 绘制效率图
plt.figure(figsize=(12, 6))
for t, values in efficiency.items():
    plt.plot(matrix_sizes, values, marker='o', label=f't={t}')
plt.title('Efficiency -- Matrix Size', fontsize=14)
plt.xlabel('Matrix Size', fontsize=12)
plt.ylabel('Efficiency', fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig('efficiency_openmp.pdf')
# 显示效率图
plt.show()
