def clean(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove column
    df = df.drop(columns=["Unnamed: 0"])

    # Fill numerical missing values
    numeric = df.select_dtypes(include="number").columns

    for col in numeric:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical missing values
    categorical = df.select_dtypes(exclude="number").columns

    for col in categorical:
        df[col] = df[col].fillna("Unknown")

    return df