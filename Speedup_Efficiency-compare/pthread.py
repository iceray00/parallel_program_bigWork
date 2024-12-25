import matplotlib.pyplot as plt

# 数据
matrix_sizes = [10, 50, 100, 200, 300, 500, 700, 1000, 1300, 1600, 2000, 2500]
# 替换后的 speedup 数据
speedup = {
    2: [0.7, 0.73, 0.81, 1.24, 1.46, 1.86, 1.81, 1.9, 1.92, 1.96, 1.97, 1.92],
    4: [0.43, 0.51, 0.56, 1.0, 1.52, 2.39, 2.83, 3.16, 3.51, 3.47, 1.83, 1.73],
    8: [0.27, 0.29, 0.33, 0.43, 1.01, 2.02, 2.27, 2.83, 3.32, 1.91, 1.82, 1.82],
    16: [0.17, 0.14, 0.18, 0.3, 0.44, 1.46, 1.97, 2.81, 3.31, 1.72, 1.71, 1.79]
}

# 替换后的 efficiency 数据
efficiency = {
    2: [0.35, 0.36, 0.41, 0.62, 0.73, 0.93, 0.9, 0.95, 0.96, 0.98, 0.98, 0.96],
    4: [0.11, 0.13, 0.14, 0.25, 0.38, 0.6, 0.71, 0.79, 0.88, 0.87, 0.46, 0.43],
    8: [0.03, 0.04, 0.04, 0.05, 0.13, 0.25, 0.28, 0.35, 0.42, 0.24, 0.23, 0.23],
    16: [0.01, 0.009, 0.011, 0.02, 0.028, 0.09, 0.12, 0.18, 0.21, 0.11, 0.11, 0.11]
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
plt.savefig('speedup_pthread.pdf')
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
plt.savefig('efficiency_pthread.pdf')
# 显示效率图
plt.show()
