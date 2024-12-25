#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


void gaussian_elimination(double** A, double* b, double* x, int n) {
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
        // 消元
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
    // 检查命令行参数
    if (argc != 2) {
        fprintf(stderr, "用法: %s <矩阵大小 N>\n", argv[0]);
        return 1;
    }

    // 获取矩阵大小 N
    int N = atoi(argv[1]);
    if (N <= 0) {
        fprintf(stderr, "矩阵大小 N 必须是正整数。\n");
        return 1;
    }

    // 动态分配矩阵和向量
    double** A = (double**)malloc(N * sizeof(double*));
    for (int i = 0; i < N; i++) {
        A[i] = (double*)malloc(N * sizeof(double));
    }
    double* b = (double*)malloc(N * sizeof(double));
    double* x = (double*)malloc(N * sizeof(double));

    // 初始化矩阵A和向量b
    srand(time(NULL));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] = rand() % 10 + 1;
        }
        A[i][i] += N; // 保证对角线占优
        b[i] = rand() % 10 + 1;
    }

    // 计时开始
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 调用高斯消元
    gaussian_elimination(A, b, x, N);

    // 计时结束
    clock_gettime(CLOCK_MONOTONIC, &end);
    double time_taken = (end.tv_sec - start.tv_sec) +
                        (end.tv_nsec - start.tv_nsec) / 1e9;
    printf("串行高斯消元时间 (矩阵规模为: %d): %f 秒\n", N, time_taken);

    // 释放内存
    for (int i = 0; i < N; i++) {
        free(A[i]);
    }
    free(A);
    free(b);
    free(x);

    return 0;
}
