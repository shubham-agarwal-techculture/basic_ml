def engineer(df):

    # Example feature

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) >= 2:
        df["sum_feature"] = df[numeric[0]] + df[numeric[1]]

    return df