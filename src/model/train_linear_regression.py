from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
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

    score = r2_score(y_test, pred)

    joblib.dump(
        model,
        "models/linear_regression.pkl"
    )

    print(
        f"\nLinear Regression R2 Score: {score:.4f}"
    )

    return score