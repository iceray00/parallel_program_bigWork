
## Dependencies

请在终端中执行下列指令以安装相应的依赖库：
```bash
pip3 install -r requirements.txt
```

## Tree

* 项目的tree结构为：

```
.
├── README.md
├── Speedup_Efficiency-compare
│   ├── compare.py
│   ├── draw_all.py
│   ├── draw_o_p_compare.py
│   ├── efficiency_bar_multiple_matrix_sizes.png
│   ├── efficiency_comparison.pdf
│   ├── efficiency_comparison_multiple_matrix_sizes.png
│   ├── efficiency_matrix_comparison.pdf
│   ├── efficiency_mpi.pdf
│   ├── efficiency_openmp.pdf
│   ├── efficiency_pthread.pdf
│   ├── efficiency_trends_all_matrix_sizes.png
│   ├── mpi.py
│   ├── openmp.py
│   ├── pthread.py
│   ├── speedup_bar_multiple_matrix_sizes.png
│   ├── speedup_comparison.pdf
│   ├── speedup_comparison_multiple_matrix_sizes.png
│   ├── speedup_matrix_comparison.pdf
│   ├── speedup_mpi.pdf
│   ├── speedup_openmp.pdf
│   ├── speedup_pthread.pdf
│   └── speedup_trends_all_matrix_sizes.png
├── exec_inMacOS
│   ├── chuanxing
│   ├── mpi
│   ├── openmp
│   └── pthread
├── results
│   ├── MPI_log.pdf
│   ├── MPI_x.pdf
│   ├── OpenMP_log.pdf
│   ├── OpenMP_x.pdf
│   ├── Pthreads_log.pdf
│   ├── Pthreads_x.pdf
│   ├── chuanxing.csv
│   ├── draw_chuanxing.py
│   ├── draw_log.py
│   ├── draw_x.py
│   ├── mpi.csv
│   ├── openmp.csv
│   ├── pthread.csv
│   ├── results.txt
│   ├── serial_execution_time_log.pdf
│   └── serial_execution_time_x.pdf
├── script
│   ├── run_chuanxing.sh
│   ├── run_mpi.sh
│   ├── run_openmp.sh
│   └── run_pthread.sh
└── src
    ├── chuanxing.c
    ├── mpi.c
    ├── openmp.c
    └── pthread.c

6 directories, 51 files
```


### 1. 根目录
- **README.md**：说明文档（本文档），用来介绍这是干啥的，各部分包含的内容。

### 2. Speedup_Efficiency-compare
此目录用于比较不同并行编程模型的加速比（Speedup）和效率（Efficiency）。
- **Python脚本**：
  - `compare.py`：用于整体比较不同模型的性能。
  - `draw_all.py`：绘制所有相关的图表。
  - `draw_o_p_compare.py`：专门用于绘制OpenMP和Pthreads的对比图。
  - `mpi.py`、`openmp.py`、`pthread.py`：分别处理MPI、OpenMP和Pthreads的性能数据。
- **图表与报告**：
  - 各种PNG和PDF文件，如`efficiency_comparison.pdf`、`speedup_trends_all_matrix_sizes.png`等，展示不同模型在多种矩阵规模下的效率和加速比对比分析。

### 3. exec_inMacOS
该目录包含在MacOS系统上执行不同并行编程模型的可执行文件。
- **可执行文件**：
  - `chuanxing`：串行执行版本。
  - `mpi`：基于MPI的并行执行版本。
  - `openmp`：基于OpenMP的并行执行版本。
  - `pthread`：基于Pthreads的并行执行版本。

### 4. results
存放各类运行结果和可视化脚本。
- **结果文件**：
  - `MPI_log.pdf`、`OpenMP_log.pdf`、`Pthreads_log.pdf`等：用于生成性能分析图表，以对数log作为坐标系。
  - `chuanxing.csv`、`mpi.csv`、`openmp.csv`、`pthread.csv`：不同模型的性能数据。
  - `results.txt`：综合的运行结果摘要。
- **绘图脚本**：
  - `draw_chuanxing.py`、`draw_log.py`、`draw_x.py`：用于生成性能分析图表，是在正常坐标系下。
- **序列执行时间**：
  - `serial_execution_time_log.pdf`、`serial_execution_time_x.pdf`：单独对于串行数据的图表展示，log为对数坐标系下的，x为正常坐标系下的。

### 5. script
包含用于运行不同并行模型的脚本文件。
- **Shell脚本**：
  - `run_chuanxing.sh`：执行串行版本。
  - `run_mpi.sh`：执行MPI并行版本。
  - `run_openmp.sh`：执行OpenMP并行版本。
  - `run_pthread.sh`：执行Pthreads并行版本。

### 6. src
存放项目的源代码文件。
- **C源文件**：
  - `chuanxing.c`：串行执行的主程序。
  - `mpi.c`：基于MPI的并行实现。
  - `openmp.c`：基于OpenMP的并行实现。
  - `pthread.c`：基于Pthreads的并行实现。

### 总结
整个项目主要分为以下几个部分：

- **README.md** 提供项目的基本信息。
- **Speedup_Efficiency-compare** 目录专注于性能比较和可视化分析。
- **exec_inMacOS** 包含在MacOS上运行的不同版本的可执行文件。
- **results** 汇总了所有运行结果、绘图脚本，便于后续分析。
- **script** 提供便捷的脚本，帮助用户快速运行各个版本。
- **src** 存放核心的源代码，分别实现了不同的并行编程模型。


