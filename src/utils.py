import pandas as pd


def load_data(path):
    """
    Loads xy_data.csv and returns Nx2 numpy array.
    """

    df = pd.read_csv(path)

    if "x" not in df.columns or "y" not in df.columns:
        raise ValueError("CSV must contain x and y columns.")

    return df[["x", "y"]].values