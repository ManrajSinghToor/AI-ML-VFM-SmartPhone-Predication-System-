import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/featured_data.csv")

# Top Brands

plt.figure(figsize=(10,5))
df["Company Name"].value_counts().head(10).plot(kind="bar")
plt.title("Top Brands")
plt.tight_layout()
plt.savefig("outputs/top_brands.png")
plt.close()

# Price Distribution

plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=20)
plt.title("Price Distribution")
plt.tight_layout()
plt.savefig("outputs/price_distribution.png")
plt.close()

# RAM vs Price

plt.figure(figsize=(8,5))
plt.scatter(df["RAM"], df["Price"])
plt.xlabel("RAM")
plt.ylabel("Price")
plt.title("RAM vs Price")
plt.tight_layout()
plt.savefig("outputs/ram_vs_price.png")
plt.close()

# Battery vs Price

plt.figure(figsize=(8,5))
plt.scatter(df["Battery Capacity"], df["Price"])
plt.xlabel("Battery")
plt.ylabel("Price")
plt.title("Battery vs Price")
plt.tight_layout()
plt.savefig("outputs/battery_vs_price.png")
plt.close()

print("Graphs Saved")