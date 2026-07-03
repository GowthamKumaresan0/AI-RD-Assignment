import numpy as np
from scipy.spatial import cKDTree


def order_points(points):
    """
    Orders an unordered point cloud by greedily following
    the nearest unvisited neighbour.
    """

    tree = cKDTree(points)

    # Start from the left-most point
    start = np.argmin(points[:, 0])

    ordered = [start]
    visited = np.zeros(len(points), dtype=bool)
    visited[start] = True

    current = start

    while len(ordered) < len(points):

        # Ask for several nearest neighbours
        _, idx = tree.query(points[current], k=20)

        next_idx = None

        for i in idx:

            if not visited[i]:
                next_idx = i
                break

        # Fallback
        if next_idx is None:

            remaining = np.where(~visited)[0]

            d = np.linalg.norm(
                points[remaining] - points[current],
                axis=1
            )

            next_idx = remaining[np.argmin(d)]

        ordered.append(next_idx)
        visited[next_idx] = True
        current = next_idx

    return points[ordered]