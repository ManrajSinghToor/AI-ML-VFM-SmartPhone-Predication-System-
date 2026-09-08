import pandas as pd
import matplotlib.pyplot as plt

def clean_data(df):

    before_rows = len(df)

    print("\n===== MISSING VALUES BEFORE CLEANING =====")
    print(df.isnull().sum())

    missing_before = df.isnull().sum().sum()

    # Remove duplicates
    df = df.drop_duplicates()

    numeric_cols = [
        "RAM",
        "Storage",
        "Front Camera",
        "Back Camera",
        "Price"
    ]

    for col in numeric_cols:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

        df[col] = df[col].fillna(
            df[col].median()
        )

    after_rows = len(df)

    print("\n===== MISSING VALUES AFTER CLEANING =====")
    print(df.isnull().sum())

    missing_after = df.isnull().sum().sum()

    print("\n===== DATA CLEANING =====")
    print("Rows Before Cleaning :", before_rows)
    print("Rows After Cleaning  :", after_rows)
    print("Rows Removed         :", before_rows - after_rows)

    # ----------------------------
    # Data Cleaning Graph
    # ----------------------------

    plt.figure(figsize=(6,4))

    plt.bar(
        ["Before Cleaning", "After Cleaning"],
        [before_rows, after_rows]
    )

    plt.title("Dataset Size Before vs After Cleaning")
    plt.ylabel("Number of Rows")

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/data_cleaning_comparison.png"
    )

    plt.close()

    # ----------------------------
    # Missing Values Graph
    # ----------------------------

    plt.figure(figsize=(6,4))

    plt.bar(
        ["Before", "After"],
        [missing_before, missing_after]
    )

    plt.title("Missing Values Handling")
    plt.ylabel("Missing Values Count")

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/missing_values_handling.png"
    )

    plt.close()

    return df