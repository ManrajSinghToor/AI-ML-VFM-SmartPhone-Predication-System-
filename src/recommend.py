import pandas as pd
import joblib

model = joblib.load("models/model.pkl")

print("\n===== Smartphone Recommendation System =====\n")

budget = float(input("Enter Budget (₹): "))
ram = float(input("Enter RAM (GB): "))
storage = float(input("Enter Storage (GB): "))
front = float(input("Enter Front Camera (MP): "))
back = float(input("Enter Back Camera (MP): "))

user_data = pd.DataFrame(
    [[
        ram,
        storage,
        front,
        back,
        budget
    ]],
    columns=[
        "RAM",
        "Storage",
        "Front Camera",
        "Back Camera",
        "Price"
    ]
)

predicted_score = model.predict(user_data)[0]

print("\nPredicted Value Score:", round(predicted_score, 2))

phones = pd.read_csv("dataset/featured_data.csv")

phones = phones[
    (phones["Price"] <= budget * 1.2)
    &
    (phones["Price"] >= budget * 0.8)
]

phones["Difference"] = abs(
    phones["Value_Score"] - predicted_score
)

recommendations = phones.sort_values(
    by="Difference"
).head(5)

print("\n===== Top 5 Recommended Phones =====\n")

print(
    recommendations[
        [
            "Company Name",
            "Model Name",
            "RAM",
            "Storage",
            "Front Camera",
            "Back Camera",
            "Price"
        ]
    ]
)