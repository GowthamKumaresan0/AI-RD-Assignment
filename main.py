from src.utils import load_data
from src.order_points import order_points
from src.optimizer import CurveOptimizer


def main():

    points = load_data("data/xy_data.csv")

    ordered = order_points(points)

    optimizer = CurveOptimizer(ordered)

    result = optimizer.optimize()

    theta, M, X = result.x

    print("\nOptimization Finished")
    print("---------------------")
    print(f"Theta : {theta:.8f}")
    print(f"M     : {M:.8f}")
    print(f"X     : {X:.8f}")
    print(f"Loss  : {result.fun:.8f}")


if __name__ == "__main__":
    main()