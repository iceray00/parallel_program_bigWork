import matplotlib.pyplot as plt
import seaborn as sns

# 设置Seaborn样式
sns.set(style="whitegrid")

# 串行数据
serial_data = {
    10: 0.000004,
    50: 0.000210,
    100: 0.001300,
    200: 0.008769,
    300: 0.024445,
    500: 0.112066,
    700: 0.304488,
    1000: 0.890970,
    1300: 1.944944,
    1600: 3.618125,
    2000: 7.034368,
    2500: 13.769433
}

# 获取所有的矩阵规模
matrix_sizes = sorted(serial_data.keys())

# 绘制串行数据图像
plt.figure(figsize=(12, 8))
serial_times = [serial_data[size] for size in matrix_sizes]

plt.plot(matrix_sizes, serial_times, marker='s', linestyle='-', color='blue', label='Serial Execution')

plt.xlabel('Matrix Size')
plt.ylabel('Run Time (seconds)')
plt.title('Serial Execution Time of Gaussian Elimination')
plt.legend()
# plt.xscale('log', base=3)
plt.yscale('log', base=3)
plt.tight_layout()
# plt.savefig('serial_execution_time_x.pdf')
plt.show()
