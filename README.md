# AI R&D Internship Assignment

## Overview

This project presents a solution for an AI Research and Development internship assignment. The objective is to estimate the unknown parameters of a parametric curve from a set of unordered two-dimensional points. The solution reconstructs the curve, models the mathematical relationship, and estimates the unknown parameters using numerical optimization techniques.

---

## Problem Statement

The given parametric equations are

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

where

| Parameter | Range |
|-----------|-------|
| $t$ | $6 \le t \le 60$ |
| $\theta$ | $0^\circ < \theta < 50^\circ$ |
| $M$ | $-0.05 < M < 0.05$ |
| $X$ | $0 < X < 100$ |

The objective is to estimate the unknown values of **θ**, **M**, and **X** that best reproduce the provided dataset.

---

## Methodology

The implemented solution follows these steps:

1. Load the dataset containing unordered 2D points.
2. Recover a continuous ordering of the points using a nearest-neighbor traversal.
3. Define the mathematical model of the parametric curve.
4. Formulate an optimization objective based on the reconstruction error.
5. Estimate the unknown parameters using the Differential Evolution algorithm provided by SciPy.

---

## Technologies Used

- Python 3
- NumPy
- Pandas
- SciPy
- Matplotlib

---

## Current Results

Estimated parameters:

| Parameter | Value |
|-----------|--------:|
| θ | 30.04470981° |
| M | 0.03001465 |
| X | 55.02232105 |

Average reconstruction loss:

```
0.24447060
```

These values represent the current optimization result obtained from the implemented pipeline.

---

## How to Run

Install the required packages

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---
# AI R&D Internship Assignment

## Overview

This project presents a solution for an AI Research and Development internship assignment. The objective is to estimate the unknown parameters of a parametric curve from a set of unordered two-dimensional points. The solution reconstructs the curve, models the mathematical relationship, and estimates the unknown parameters using numerical optimization techniques.

---

## Problem Statement

The given parametric equations are

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

where

| Parameter | Range |
|-----------|-------|
| $t$ | $6 \le t \le 60$ |
| $\theta$ | $0^\circ < \theta < 50^\circ$ |
| $M$ | $-0.05 < M < 0.05$ |
| $X$ | $0 < X < 100$ |

The objective is to estimate the unknown values of **θ**, **M**, and **X** that best reproduce the provided dataset.

---

## Methodology

The implemented solution follows these steps:

1. Load the dataset containing unordered 2D points.
2. Recover a continuous ordering of the points using a nearest-neighbor traversal.
3. Define the mathematical model of the parametric curve.
4. Formulate an optimization objective based on the reconstruction error.
5. Estimate the unknown parameters using the Differential Evolution algorithm provided by SciPy.

---

## Technologies Used

- Python 3
- NumPy
- Pandas
- SciPy
- Matplotlib

---

## Current Results

Estimated parameters:

| Parameter | Value |
|-----------|--------:|
| θ | 30.04470981° |
| M | 0.03001465 |
| X | 55.02232105 |

Average reconstruction loss:

```
0.24447060
```

These values represent the current optimization result obtained from the implemented pipeline.

---

## How to Run

Install the required packages

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## References

1. Virtanen, P., et al. (2020). *SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python*. Nature Methods, 17, 261–272.

2. Harris, C. R., et al. (2020). *Array Programming with NumPy*. Nature, 585, 357–362.

3. McKinney, W. (2010). *Data Structures for Statistical Computing in Python*. Proceedings of the 9th Python in Science Conference.

4. Hunter, J. D. (2007). *Matplotlib: A 2D Graphics Environment*. Computing in Science & Engineering.

5. The mathematical formulation and parameter constraints are taken directly from the internship assignment document provided by the organization.

---

## Author

**Gowtham Kumaresan**

B.Tech – Artificial Intelligence and Data Science

Amrita Vishwa Vidyapeetham
