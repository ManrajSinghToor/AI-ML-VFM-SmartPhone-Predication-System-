import pandas as pd

df = pd.read_csv("dataset/cleaned_data.csv")

df["Value_Score"] = (
    (
        df["RAM"] * 0.30
        + df["Storage"] * 0.25
        + df["Back Camera"] * 0.25
        + df["Front Camera"] * 0.20
    )
    / df["Price"]
) * 100000

# Remove rows containing NaN
df = df.dropna()

df.to_csv("dataset/featured_data.csv", index=False)

print("Feature Engineering Complete")
print("Shape:", df.shape)
print(df.isnull().sum())