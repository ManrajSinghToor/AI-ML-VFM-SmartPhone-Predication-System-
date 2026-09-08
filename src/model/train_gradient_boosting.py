from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error
)
from sklearn.preprocessing import StandardScaler

import joblib


def train_gradient_boosting(X, y):

    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    scaler = StandardScaler()

# Save original values  
    before_scaling = pd.DataFrame(
        X,
        columns=[
            "RAM",
            "Storage",
            "Front Camera",
            "Back Camera",
            "Price"
        ]
    )

    X = scaler.fit_transform(X)

# Save scaled values
    after_scaling = pd.DataFrame(
        X,
        columns=[
            "RAM",
            "Storage",
            "Front Camera",
            "Back Camera",
            "Price"
        ]
    )

    print("\n===== BEFORE SCALING =====")
    print(before_scaling.head())

    print("\n===== AFTER SCALING =====")
    print(after_scaling.head())

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    

    model = GradientBoostingRegressor(
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    pred = model.predict(
        X_test
    )

    r2 = r2_score(
        y_test,
        pred
    )

    mae = mean_absolute_error(
        y_test,
        pred
    )

    joblib.dump(
        model,
        "models/gradient_boosting.pkl"
    )

    joblib.dump(
        scaler,
        "models/scaler.pkl"
    )

    print("\n===== Gradient Boosting =====")

    print(
        f"R² Score : {r2:.4f}"
    )

    print(
        f"MAE      : {mae:.4f}"
    )

    return r2