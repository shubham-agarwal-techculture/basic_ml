from pathlib import Path
import pandas as pd


def save_dataset(X, y, path):

    df = X.copy()
    df["target"] = y

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)