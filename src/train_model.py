import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("dataset/featured_data.csv")

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

score = r2_score(y_test, pred)

print("R2 Score:", score)

joblib.dump(model, "models/model.pkl")

print("Model Saved")

# Actual vs Predicted

plt.figure(figsize=(8,5))
plt.scatter(y_test, pred)
plt.xlabel("Actual Value Score")
plt.ylabel("Predicted Value Score")
plt.title("Actual vs Predicted")
plt.tight_layout()
plt.savefig("outputs/actual_vs_predicted.png")
plt.close()

# Feature Importance

importance = model.feature_importances_

plt.figure(figsize=(8,5))
plt.bar(X.columns, importance)
plt.title("Feature Importance")
plt.tight_layout()
plt.savefig("outputs/feature_importance.png")
plt.close()

print("Graphs Saved")