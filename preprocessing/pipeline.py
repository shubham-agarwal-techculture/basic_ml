from config import *

from preprocessing.load import load_data
from preprocessing.inspect import inspect
from preprocessing.clean import clean
from preprocessing.transform import transform
from preprocessing.engineer import engineer
from preprocessing.select import select_features
from preprocessing.split import split
from preprocessing.save import save_dataset


def run_pipeline():

    # Load
    df = load_data(RAW_FILE)

    # Inspect
    inspect(df)

    # Clean
    df = clean(df)

    # Transform
    df = transform(df)

    # Feature Engineering
    df = engineer(df)

    # Feature Selection
    df = select_features(df)

    # Split
    (
        X_train,
        X_valid,
        X_test,
        y_train,
        y_valid,
        y_test,
    ) = split(df)

    # Save
    save_dataset(
        X_train,
        y_train,
        PROCESSED_DIR / "train.csv",
    )

    save_dataset(
        X_valid,
        y_valid,
        PROCESSED_DIR / "valid.csv",
    )

    save_dataset(
        X_test,
        y_test,
        PROCESSED_DIR / "test.csv",
    )

    print("Pipeline Complete")