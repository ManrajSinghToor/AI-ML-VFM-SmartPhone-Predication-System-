import pandas as pd

df = pd.read_csv("dataset/smartphones.csv")

numeric_cols = [
    "RAM",
    "Storage",
    "Front Camera",
    "Back Camera",
    "Price"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col].fillna(df[col].median(), inplace=True)

df = df.drop_duplicates()

df.to_csv("dataset/cleaned_data.csv", index=False)

print("Data Cleaning Complete")
print("Shape:", df.shape)