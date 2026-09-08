from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error
)
import joblib


def train_random_forest(X, y):

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
        "models/random_forest.pkl"
    )

    print("\n===== Random Forest =====")

    print(f"R² Score : {r2:.4f}")

    print(f"MAE      : {mae:.4f}")

    return r2