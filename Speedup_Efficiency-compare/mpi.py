import matplotlib.pyplot as plt

# 数据
matrix_sizes = [10, 50, 100, 200, 300, 500, 700, 1000, 1300, 1600, 2000, 2500]
# 替换后的 speedup 数据
speedup = {
    2: [0, 0.19, 1.51, 1.96, 1.74, 1.82, 2.58, 2, 2.03, 1.99, 1.98, 1.94],
    4: [0, 0.39, 1.14, 2.13, 2.93, 3.25, 4.95, 3.94, 3.91, 3.85, 1.66, 1.4],
    6: [0, 0.08, 0.36, 2.1, 1.4, 1.96, 2.92, 2.53, 2.55, 1.18, 0.69, 0.79]
}

# 替换后的 efficiency 数据
efficiency = {
    2: [0, 0.09, 0.75, 0.98, 0.87, 0.91, 1.29, 1, 1.02, 1, 0.99, 0.97],
    4: [0, 0.1, 0.29, 0.53, 0.73, 0.81, 1.24, 0.99, 0.98, 0.96, 0.42, 0.35],
    6: [0, 0.01, 0.06, 0.35, 0.23, 0.33, 0.49, 0.42, 0.43, 0.2, 0.12, 0.13]
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
plt.savefig('speedup_mpi.pdf')
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
plt.savefig('efficiency_mpi.pdf')
# 显示效率图
plt.show()
