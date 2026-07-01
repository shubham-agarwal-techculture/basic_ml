def inspect(df):
    print("=" * 60)
    print("Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nDtypes")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isna().sum())

    print("\nDuplicates")
    print(df.duplicated().sum())

    print("\nStatistics")
    print(df.describe(include="all"))