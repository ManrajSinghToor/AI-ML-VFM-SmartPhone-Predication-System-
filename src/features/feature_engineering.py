from src.visualization.generate_graphs import generate_graphs

def feature_engineering(df):

    print("\nCreating Value Score...")

    df["Value_Score"] = (
        (
            df["RAM"] * 0.30
            + df["Storage"] * 0.25
            + df["Back Camera"] * 0.25
            + df["Front Camera"] * 0.20
        )
        / df["Price"]
    ) * 100000

    generate_graphs(df)

    return df