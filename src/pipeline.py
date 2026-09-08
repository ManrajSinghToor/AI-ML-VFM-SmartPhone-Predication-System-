from src.data.load_data import load_data
from src.preprocessing.clean_data import clean_data
from src.features.feature_engineering import feature_engineering
from src.data.inspect_data import inspect_data

df = load_data()
df = clean_data(df)
df = feature_engineering(df)
inspect_data(df)

df.to_csv(
    "dataset/featured_data.csv",
    index=False
)

print("\nfeatured_data.csv created successfully")
print("Shape:", df.shape)