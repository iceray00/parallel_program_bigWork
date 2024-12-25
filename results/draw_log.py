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

# OpenMP数据
openmp_data = {
    10: {1: 0.003213, 2: 0.000829, 4: 0.000728, 8: 0.000897, 16: 0.001277},
    50: {1: 0.000591, 2: 0.000796, 4: 0.001024, 8: 0.001998, 16: 0.003441},
    100: {1: 0.001495, 2: 0.001638, 4: 0.001794, 8: 0.002794, 16: 0.005264},
    200: {1: 0.009255, 2: 0.006472, 4: 0.004952, 8: 0.007332, 16: 0.012193},
    300: {1: 0.029914, 2: 0.018618, 4: 0.012017, 8: 0.015772, 16: 0.025023},
    500: {1: 0.141495, 2: 0.076131, 4: 0.054442, 8: 0.052341, 16: 0.065361},
    700: {1: 0.426103, 2: 0.201693, 4: 0.111760, 8: 0.123117, 16: 0.292750},
    1000: {1: 1.101658, 2: 0.576008, 4: 0.341426, 8: 0.478744, 16: 0.578477},
    1300: {1: 2.403546, 2: 1.262892, 4: 1.038058, 8: 1.365485, 16: 1.469483},
    1600: {1: 4.453914, 2: 2.365714, 4: 1.749789, 8: 2.352645, 16: 2.115870},
    2000: {1: 8.643443, 2: 4.503185, 4: 3.747577, 8: 4.463509, 16: 4.277102},
    2500: {1: 16.845193, 2: 8.864100, 4: 7.638869, 8: 8.659751, 16: 8.178104}
}

# Pthreads数据
pthread_data = {
    10: {1: 0.000362, 2: 0.000517, 4: 0.000833, 8: 0.001330, 16: 0.002131},
    50: {1: 0.001268, 2: 0.001727, 4: 0.002477, 8: 0.004397, 16: 0.008965},
    100: {1: 0.003032, 2: 0.003734, 4: 0.005433, 8: 0.009198, 16: 0.017118},
    200: {1: 0.011116, 2: 0.008940, 4: 0.011139, 8: 0.025693, 16: 0.036647},
    300: {1: 0.029754, 2: 0.020391, 4: 0.019615, 8: 0.029422, 16: 0.067532},
    500: {1: 0.135312, 2: 0.072496, 4: 0.056541, 8: 0.066934, 16: 0.092705},
    700: {1: 0.319639, 2: 0.176166, 4: 0.112960, 8: 0.140624, 16: 0.162131},
    1000: {1: 0.913091, 2: 0.480200, 4: 0.289014, 8: 0.322928, 16: 0.325008},
    1300: {1: 1.973827, 2: 1.025188, 4: 0.562010, 8: 0.593914, 16: 0.595094},
    1600: {1: 3.674233, 2: 1.874412, 4: 1.057547, 8: 1.917862, 16: 2.132015},
    2000: {1: 7.086054, 2: 3.604779, 4: 3.876557, 8: 3.890121, 16: 4.142054},
    2500: {1: 13.782271, 2: 7.173998, 4: 7.963377, 8: 7.553834, 16: 7.684634}
}

# MPI数据
mpi_data = {
    10: {1: 0.000002, 2: 0.001079, 4: 0.000882, 6: 0.001521},
    50: {1: 0.000140, 2: 0.001130, 4: 0.000540, 6: 0.002640},
    100: {1: 0.001003, 2: 0.000859, 4: 0.001139, 6: 0.003564},
    200: {1: 0.007913, 2: 0.004470, 4: 0.004119, 6: 0.004170},
    300: {1: 0.026316, 2: 0.014066, 4: 0.008351, 6: 0.017430},
    500: {1: 0.120230, 2: 0.061544, 4: 0.034542, 6: 0.057070},
    700: {1: 0.327025, 2: 0.165582, 4: 0.086090, 6: 0.146007},
    1000: {1: 0.960975, 2: 0.478967, 4: 0.244063, 6: 0.379824},
    1300: {1: 2.120820, 2: 1.045478, 4: 0.542065, 6: 0.831649},
    1600: {1: 3.878526, 2: 1.947992, 4: 1.007589, 6: 3.277600},
    2000: {1: 7.575693, 2: 3.818565, 4: 4.568192, 6: 10.912373},
    2500: {1: 14.771811, 2: 7.597270, 4: 10.518386, 6: 18.643718}
}

# 获取所有的矩阵规模
matrix_sizes = sorted(serial_data.keys())

# 获取所有的线程数和进程数
openmp_threads = sorted({threads for data in openmp_data.values() for threads in data.keys()})
pthread_threads = sorted({threads for data in pthread_data.values() for threads in data.keys()})
mpi_processes = sorted({procs for data in mpi_data.values() for procs in data.keys()})


# 绘图函数
def plot_parallel_log(data, parallel_type, thread_or_proc_counts, matrix_sizes, serial_data):
    plt.figure(figsize=(12, 10))

    for count in thread_or_proc_counts:
        times = []
        for size in matrix_sizes:
            if count in data[size]:
                times.append(data[size][count])
            else:
                times.append(None)  # 如果某个线程数或进程数在特定矩阵规模下没有数据
        plt.plot(matrix_sizes, times, marker='o',
                 label=f'{parallel_type} {"Thread" if parallel_type != "MPI" else "Process"}={count}')

    # 绘制串行数据作为参考
    serial_times = [serial_data[size] for size in matrix_sizes]
    plt.plot(matrix_sizes, serial_times, marker='s', linestyle='--', color='black', label='Serial (ChuanXing)')

    plt.xlabel('Matrix size')
    plt.ylabel('Run Time (seconds)')
    plt.title(f'{parallel_type} Comparison of running times of Gaussian elimination')
    plt.legend()
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.tight_layout()
    plt.savefig(f'{parallel_type}_log.pdf')
    plt.show()


# 绘制串行和OpenMP的比较
plot_parallel_log(openmp_data, 'OpenMP', openmp_threads, matrix_sizes, serial_data)

# 绘制串行和Pthreads的比较
plot_parallel_log(pthread_data, 'Pthreads', pthread_threads, matrix_sizes, serial_data)

# 绘制串行和MPI的比较
plot_parallel_log(mpi_data, 'MPI', mpi_processes, matrix_sizes, serial_data)



