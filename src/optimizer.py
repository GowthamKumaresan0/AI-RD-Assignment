import numpy as np
from scipy.optimize import differential_evolution
from src.model import ParametricCurve


class CurveOptimizer:

    def __init__(self, target_points):

        self.target = target_points
        self.N = len(target_points)

        self.t = np.linspace(6, 60, self.N)

    def objective(self, params):

        theta, M, X = params

        curve = ParametricCurve(theta, M, X)

        predicted = curve.evaluate(self.t)

        return np.mean(
            np.linalg.norm(
                predicted - self.target,
                axis=1
            )
        )

    def optimize(self):

        bounds = [
            (0, 50),
            (-0.05, 0.05),
            (0, 100)
        ]

        result = differential_evolution(
            self.objective,
            bounds=bounds,
            maxiter=300,
            popsize=20,
            polish=True,
            workers=1,
            seed=42
        )

        return result