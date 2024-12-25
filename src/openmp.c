#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <omp.h>

#define BILLION 1000000000.0

void gaussian_elimination_omp(double** A, double* b, double* x, int n, int num_threads) {
    omp_set_num_threads(num_threads);
    for(int k = 0; k < n-1; k++) {
        // 选择主元
        double max = fabs(A[k][k]);
        int max_row = k;
        for(int i = k+1; i < n; i++) {
            if(fabs(A[i][k]) > max) {
                max = fabs(A[i][k]);
                max_row = i;
            }
        }
        // 交换行
        if(max_row != k) {
            double* temp = A[k];
            A[k] = A[max_row];
            A[max_row] = temp;
            double temp_b = b[k];
            b[k] = b[max_row];
            b[max_row] = temp_b;
        }
        // 并行消元
        #pragma omp parallel for
        for(int i = k+1; i < n; i++) {
            double factor = A[i][k] / A[k][k];
            A[i][k] = 0.0;
            for(int j = k+1; j < n; j++) {
                A[i][j] -= factor * A[k][j];
            }
            b[i] -= factor * b[k];
        }
    }
    // 回代
    for(int i = n-1; i >= 0; i--) {
        x[i] = b[i];
        for(int j = i+1; j < n; j++) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] /= A[i][i];
    }
}

int main(int argc, char* argv[]) {
    if(argc != 3){
        printf("Usage: %s <matrix_size> <num_threads>\n", argv[0]);
        return -1;
    }
    int N = atoi(argv[1]);
    int num_threads = atoi(argv[2]);

    // 动态分配矩阵和向量
    double** A = (double**)malloc(N * sizeof(double*));
    for(int i = 0; i < N; i++) {
        A[i] = (double*)malloc(N * sizeof(double));
    }
    double* b = (double*)malloc(N * sizeof(double));
    double* x = (double*)malloc(N * sizeof(double));

    // 初始化矩阵A和向量b
    srand(time(NULL));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            A[i][j] = rand() % 10 + 1;
        }
        A[i][i] += N; // 保证对角线占优
        b[i] = rand() % 10 + 1;
    }

//    // 计时开始
//    double start_time = omp_get_wtime();

    struct timespec start, end;

    // 开始时间
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 调用OpenMP高斯消元
    gaussian_elimination_omp(A, b, x, N, num_threads);

    // 计时结束
//    double end_time = omp_get_wtime();
//    double time_taken = end_time - start_time;

    // 结束时间
    clock_gettime(CLOCK_MONOTONIC, &end);

    // 计算运行时间
    double elapsed_time = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / BILLION;

    printf("OpenMP高斯消元时间 (矩阵规模: %d, 线程数: %d): %f 秒\n", N, num_threads, elapsed_time);

    // 释放内存
    for(int i = 0; i < N; i++) {
        free(A[i]);
    }
    free(A);
    free(b);
    free(x);

    return 0;
}
