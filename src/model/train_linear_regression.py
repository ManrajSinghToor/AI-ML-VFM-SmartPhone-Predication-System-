from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error
)
import joblib


def train_linear_regression(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

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
        "models/linear_regression.pkl"
    )

    print("\n===== Linear Regression =====")

    print(f"R² Score : {r2:.4f}")

    print(f"MAE      : {mae:.4f}")

    return r2