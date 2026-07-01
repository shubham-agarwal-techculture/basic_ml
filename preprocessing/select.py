def select_features(df):

    # Example:
    # Drop ID column if present

    if "id" in df.columns:
        df = df.drop(columns=["id"])

    return df