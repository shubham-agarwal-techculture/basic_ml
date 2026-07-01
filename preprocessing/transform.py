from sklearn.preprocessing import StandardScaler


def transform(df):
    numeric = df.select_dtypes(include="number").columns

    scaler = StandardScaler()

    df[numeric] = scaler.fit_transform(df[numeric])

    return df