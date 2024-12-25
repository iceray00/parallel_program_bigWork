#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <mpi.h>

#define BILLION 1000000000.0

int main(int argc, char* argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (argc < 2) {  // 判断是否提供了矩阵规模
        if (rank == 0) {
            printf("用法: %s 矩阵规模\n", argv[0]);
        }
        MPI_Finalize();
        return 1;
    }

    int N = atoi(argv[1]);

    double** A = NULL;
    double* b = NULL;
    double* x = NULL;
    if(rank == 0) {
        // 动态分配矩阵和向量
        A = (double**)malloc(N * sizeof(double*));
        for(int i = 0; i < N; i++) {
            A[i] = (double*)malloc(N * sizeof(double));
        }
        b = (double*)malloc(N * sizeof(double));
        x = (double*)malloc(N * sizeof(double));

        // 初始化矩阵A和向量b
        srand(time(NULL));
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                A[i][j] = rand() % 10 + 1;
            }
            A[i][i] += N; // 保证对角线占优
            b[i] = rand() % 10 + 1;
        }
    }

    // 广播矩阵A和向量b到所有进程
    double* flat_A = NULL;
    if(rank == 0) {
        flat_A = (double*)malloc(N * N * sizeof(double));
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                flat_A[i*N + j] = A[i][j];
            }
        }
    } else {
        flat_A = (double*)malloc(N * N * sizeof(double));
        b = (double*)malloc(N * sizeof(double));
    }
    MPI_Bcast(flat_A, N*N, MPI_DOUBLE, 0, MPI_COMM_WORLD);
    if(rank != 0) {
        b = (double*)malloc(N * sizeof(double));
    }
    MPI_Bcast(b, N, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // 转换为二维数组
    if(rank != 0) {
        A = (double**)malloc(N * sizeof(double*));
        for(int i = 0; i < N; i++) {
            A[i] = &flat_A[i*N];
        }
    }

    x = (double*)malloc(N * sizeof(double));

//    double start_time = MPI_Wtime();

    struct timespec start, end;

    // 开始时间
    clock_gettime(CLOCK_MONOTONIC, &start);

    for(int k = 0; k < N-1; k++) {
        // 选择主元
        double max = fabs(A[k][k]);
        int max_row = k;
        for(int i = k+1; i < N; i++) {
            if(fabs(A[i][k]) > max) {
                max = fabs(A[i][k]);
                max_row = i;
            }
        }

//        // 广播主元行信息
//        double pivot = A[max_row][k];
//        MPI_Bcast(&pivot, 1, MPI_DOUBLE, max_row, MPI_COMM_WORLD);

        // 广播主元行信息
        double pivot;
        if (rank == 0) {
            pivot = A[max_row][k];
        }
        MPI_Bcast(&pivot, 1, MPI_DOUBLE, 0, MPI_COMM_WORLD);

        // 每个进程处理其分配的行
        for(int i = rank; i < N; i += size) {
            if(i > k) {
                double factor = A[i][k] / pivot;
                A[i][k] = 0.0;
                for(int j = k+1; j < N; j++) {
                    A[i][j] -= factor * A[max_row][j];
                }
                b[i] -= factor * b[max_row];
            }
        }
        MPI_Barrier(MPI_COMM_WORLD);
    }

    // 回代（仅进程0负责）
    if(rank == 0) {
        for(int i = N-1; i >= 0; i--) {
            x[i] = b[i];
            for(int j = i+1; j < N; j++) {
                x[i] -= A[i][j] * x[j];
            }
            x[i] /= A[i][i];
        }
    }

    // 结束时间
    clock_gettime(CLOCK_MONOTONIC, &end);

    // 计算运行时间
    double elapsed_time = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / BILLION;

    if(rank == 0) {
        printf("MPI高斯消元时间 (矩阵规模: %d, %d 进程): %f 秒\n", N, size, elapsed_time);
    }

    // 释放内存
    if(rank == 0) {
        for(int i = 0; i < N; i++) {
            free(A[i]);
        }
        free(A);
        free(b);
        free(x);
        free(flat_A);
    } else {
        free(A);
        free(b);
    }

    MPI_Finalize();
    return 0;
}
