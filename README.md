# AI R&D Internship Assignment

## Overview

This project is a solution for the AI Research & Development Internship Assignment.

The objective is to estimate the unknown parameters of a parametric curve from a given set of unordered 2D points. The unknown parameters are:

- θ (Theta)
- M
- X

The dataset consists of 1500 unordered `(x, y)` coordinates sampled from the following parametric equation.

## Parametric Curve

The curve is defined by the following parametric equations:

$$
x(t) = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
$$

$$
y(t) = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
$$

where

### Parameter Constraints

| Parameter | Range |
|-----------|-------|
| $t$ | $6 \le t \le 60$ |
| $\theta$ | $0^\circ < \theta < 50^\circ$ |
| $M$ | $-0.05 < M < 0.05$ |
| $X$ | $0 < X < 100$ |

The goal is to recover the unknown parameters that best reconstruct the original curve.

---

# Project Structure

```
AI-RD-Assignment/
│
├── data/
│   └── xy_data.csv
│
├── src/
│   ├── model.py
│   ├── optimizer.py
│   ├── order_points.py
│   ├── utils.py
│   └── visualize.py
│
├── output/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Approach

The solution follows these steps:

1. Load the dataset.
2. Recover a continuous ordering of the unordered points using a nearest-neighbor traversal.
3. Define the parametric curve model.
4. Estimate the unknown parameters using Differential Evolution.
5. Minimize the average Euclidean distance between predicted and observed points.

---

# Optimization

The optimization uses SciPy's Differential Evolution algorithm.

Optimization variables:

- θ ∈ [0°, 50°]
- M ∈ [-0.05, 0.05]
- X ∈ [0, 100]

Objective:

Minimize the mean Euclidean distance between predicted and observed points.

---

# Current Results

Current optimized parameters:

| Parameter | Value |
|-----------|---------:|
| θ | 30.04470981° |
| M | 0.03001465 |
| X | 55.02232105 |

Loss:

```
0.24447060
```

These values are obtained using the current optimization pipeline and serve as an initial approximation.

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running

Execute

```bash
python main.py
```

The program will:

- Load the dataset
- Order the points
- Optimize the unknown parameters
- Display the estimated values

---

# Libraries Used

- NumPy
- Pandas
- SciPy
- Matplotlib

---

# Future Improvements

Possible enhancements include:

- Arc-length parameterization
- Spline interpolation
- Local optimization refinement
- Improved point-order reconstruction
- Lower L1 reconstruction error
- Curve visualization comparing prediction and ground truth

---

# Author

**Gowtham Kumaresan**

B.Tech Artificial Intelligence and Data Science

Amrita Vishwa Vidyapeetham

---

# License

This repository is created solely for the AI Research & Development Internship Assignment.