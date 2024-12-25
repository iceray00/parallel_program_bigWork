#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <pthread.h>

#define BILLION 1000000000.0

// 定义线程数据结构
typedef struct {
    double** A;
    double* b;
    double* x;
    int n;
    int k;
    int start;
    int end;
} thread_data_t;

// 消元函数
void* eliminate(void* arg) {
    thread_data_t* data = (thread_data_t*)arg;
    double** A = data->A;
    double* b = data->b;
    int n = data->n;
    int k = data->k;
    int start = data->start;
    int end = data->end;

    for (int i = start; i < end; i++) {
        if (i > k) {
            double factor = A[i][k] / A[k][k];
            A[i][k] = 0.0;
            for (int j = k + 1; j < n; j++) {
                A[i][j] -= factor * A[k][j];
            }
            b[i] -= factor * b[k];
        }
    }

    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Usage: %s <matrix_size> <num_threads>\n", argv[0]);
        return -1;
    }

    // 从命令行获取矩阵规模 N 和线程数 num_threads
    int N = atoi(argv[1]);
    int num_threads = atoi(argv[2]);

    if (num_threads <= 0 || N <= 0) {
        printf("Error: Both matrix_size and num_threads must be positive integers.\n");
        return -1;
    }

    // 动态分配矩阵和向量
    double** A = (double**)malloc(N * sizeof(double*));
    for (int i = 0; i < N; i++) {
        A[i] = (double*)malloc(N * sizeof(double));
    }
    double* b = (double*)malloc(N * sizeof(double));
    double* x = (double*)malloc(N * sizeof(double));

    // 初始化矩阵 A 和向量 b
    srand(time(NULL));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] = rand() % 10 + 1;
        }
        A[i][i] += N; // 保证对角线占优
        b[i] = rand() % 10 + 1;
    }

    // 创建线程
    pthread_t threads[num_threads];
    thread_data_t thread_data[num_threads];
//    double start_time = (double)clock() / CLOCKS_PER_SEC;

    struct timespec start, end;

    // 开始时间
    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int k = 0; k < N - 1; k++) {
        // 选择主元
        double max = fabs(A[k][k]);
        int max_row = k;
        for (int i = k + 1; i < N; i++) {
            if (fabs(A[i][k]) > max) {
                max = fabs(A[i][k]);
                max_row = i;
            }
        }
        // 交换行
        if (max_row != k) {
            double* temp = A[k];
            A[k] = A[max_row];
            A[max_row] = temp;
            double temp_b = b[k];
            b[k] = b[max_row];
            b[max_row] = temp_b;
        }

        // 分配任务
        int rows = N - k - 1;
        int chunk = rows / num_threads;
        for (int t = 0; t < num_threads; t++) {
            thread_data[t].A = A;
            thread_data[t].b = b;
            thread_data[t].x = x;
            thread_data[t].n = N;
            thread_data[t].k = k;
            thread_data[t].start = k + 1 + t * chunk;
            thread_data[t].end = (t == num_threads - 1) ? N : k + 1 + (t + 1) * chunk;
            pthread_create(&threads[t], NULL, eliminate, (void*)&thread_data[t]);
        }

        // 等待所有线程完成
        for (int t = 0; t < num_threads; t++) {
            pthread_join(threads[t], NULL);
        }
    }

    // 回代
    for (int i = N - 1; i >= 0; i--) {
        x[i] = b[i];
        for (int j = i + 1; j < N; j++) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] /= A[i][i];
    }

//    double end_time = (double)clock() / CLOCKS_PER_SEC;
    // 结束时间
    clock_gettime(CLOCK_MONOTONIC, &end);

    // 计算运行时间
    double elapsed_time = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / BILLION;

    printf("Pthreads高斯消元时间 (矩阵规模: %d, 线程数: %d): %f 秒\n", N, num_threads, elapsed_time);

    // 释放内存
    for (int i = 0; i < N; i++) {
        free(A[i]);
    }
    free(A);
    free(b);
    free(x);

    return 0;
}
