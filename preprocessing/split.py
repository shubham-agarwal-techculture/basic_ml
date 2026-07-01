from sklearn.model_selection import train_test_split

from config import (
    TARGET,
    TRAIN_SIZE,
    RANDOM_STATE,
)


def split(df):

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    X_train, X_temp, y_train, y_temp = train_test_split(
        X,
        y,
        train_size=TRAIN_SIZE,
        random_state=RANDOM_STATE,
    )

    valid_ratio = 0.5

    X_valid, X_test, y_valid, y_test = train_test_split(
        X_temp,
        y_temp,
        train_size=valid_ratio,
        random_state=RANDOM_STATE,
    )

    return (
        X_train,
        X_valid,
        X_test,
        y_train,
        y_valid,
        y_test,
    )