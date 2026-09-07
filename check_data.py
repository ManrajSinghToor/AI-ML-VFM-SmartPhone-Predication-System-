import pandas as pd

df = pd.read_csv("dataset/smartphones.csv")

print(df.shape)
print(df.head())
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())