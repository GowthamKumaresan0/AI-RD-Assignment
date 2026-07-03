import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution

# --------------------------
# Load data
# --------------------------

data = pd.read_csv("data/xy_data.csv")

points = data[["x", "y"]].values

# Initial ordering
points = points[np.argsort(points[:,0])]

x_actual = points[:,0]
y_actual = points[:,1]

N = len(points)

t = np.linspace(6,60,N)

# --------------------------
# Parametric curve
# --------------------------

def curve(theta_deg, M, X):

    theta = np.radians(theta_deg)

    exp_term = np.exp(M*np.abs(t))
    s = np.sin(0.3*t)

    x = (
        t*np.cos(theta)
        - exp_term*s*np.sin(theta)
        + X
    )

    y = (
        42
        + t*np.sin(theta)
        + exp_term*s*np.cos(theta)
    )

    return x,y

# --------------------------
# Objective Function
# --------------------------

def objective(params):

    theta,M,X = params

    xp,yp = curve(theta,M,X)

    return np.mean(np.abs(x_actual-xp)+np.abs(y_actual-yp))

# --------------------------
# Optimization
# --------------------------

bounds = [
    (0,50),
    (-0.05,0.05),
    (0,100)
]

result = differential_evolution(
    objective,
    bounds,
    maxiter=300,
    polish=True,
    workers=-1
)

theta,M,X = result.x

print("Theta =",theta)
print("M =",M)
print("X =",X)

print("Error =",result.fun)