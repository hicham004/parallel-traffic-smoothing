# Parallel Traffic Data Smoothing

This project implements Gaussian smoothing on traffic data using different parallel programming techniques.

## Overview

The workflow is:

Raw traffic dataset → preprocessing (Python) → 2D grid → smoothing (C) → visualization

- The dataset is converted into a 2D grid:
  - X-axis: hour of the day (0–23)
  - Y-axis: weather index (from PCA)
- Each cell represents average traffic volume
- A Gaussian filter is applied to smooth the grid

## Implementations

- **Sequential (C)** – baseline version
- **OpenMP (C)** – parallel version using OpenMP directives
- **pThreads (C)** – parallel version using POSIX threads

## Results

- Sequential: ~1.10 s  
- OpenMP (best): ~0.79 s  
- pThreads (best): ~0.21 s  

pThreads achieved the best performance on this setup.

## Project Structure

```
src/        → source code (C + Python)
data/       → raw dataset
results/    → generated grid and outputs
plots/      → heatmaps
report/     → report files
```

## How to Run

### Sequential

```
gcc src/seq.c -o seq -lm
./seq
```

### OpenMP

```
gcc src/omp.c -o omp -fopenmp -lm
./omp
```

### pThreads

```
gcc src/pth.c -o pth -pthread -lm
./pth
```

### Visualization

```
python src/plot_heatmaps.py
```

## Notes

- Gaussian smoothing reduces noise in traffic data
- All implementations produce the same output values
- Performance depends on problem size and threading overhead

## Author

Hicham Saad
