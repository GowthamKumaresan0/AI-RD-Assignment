import matplotlib.pyplot as plt


def plot_points(points):

    plt.figure(figsize=(8, 8))

    plt.plot(
        points[:, 0],
        points[:, 1],
        linewidth=1
    )

    plt.scatter(
        points[:, 0],
        points[:, 1],
        s=3
    )

    plt.axis("equal")
    plt.grid(True)

    plt.show()