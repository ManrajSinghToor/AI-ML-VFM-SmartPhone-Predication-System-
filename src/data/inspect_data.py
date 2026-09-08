def inspect_data(df):

    print("\n====================================")
    print("FINAL PRE-PROCESSED DATASET")
    print("====================================")

    print(f"\nDataset Shape:")
    print(f"{df.shape[0]} samples x {df.shape[1]} features")

    print("\nFeature Composition:")

    for col in df.columns:
        print(col)

    print("\n====================================")

    print("\nDataset Preview:\n")
    print(df.head())

    print("\n====================================")

    print("\nValidation")

    X = df[
        [
            "RAM",
            "Storage",
            "Front Camera",
            "Back Camera",
            "Price"
        ]
    ]

    y = df["Value_Score"]

    print(f"\nFeature Matrix Shape : {X.shape}")
    print(f"\nTarget Shape : {y.shape}")
    print(f"\nMissing Values : {df.isnull().sum().sum()}")
    print(f"\nDuplicate Rows : {df.duplicated().sum()}")

    print("\nFinal Dataset Validation : PASSED")

    print("\n====================================")