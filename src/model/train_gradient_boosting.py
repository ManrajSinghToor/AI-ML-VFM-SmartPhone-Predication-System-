from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib


def train_gradient_boosting(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = GradientBoostingRegressor(
        random_state=42
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    score = r2_score(y_test, pred)

    joblib.dump(
        model,
        "models/gradient_boosting.pkl"
    )

    print(
        f"\nGradient Boosting R2 Score: {score:.4f}"
    )

    return score