import numpy as np


class ParametricCurve:

    def __init__(self, theta_deg, M, X):

        self.theta = np.radians(theta_deg)
        self.M = M
        self.X = X

    def evaluate(self, t):

        exp_term = np.exp(self.M * np.abs(t))
        wave = np.sin(0.3 * t)

        x = (
            t * np.cos(self.theta)
            - exp_term * wave * np.sin(self.theta)
            + self.X
        )

        y = (
            42
            + t * np.sin(self.theta)
            + exp_term * wave * np.cos(self.theta)
        )

        return np.column_stack((x, y))