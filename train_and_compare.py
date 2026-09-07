from src.data.load_data import load_data

from src.preprocessing.preprocess_pipeline import (
    preprocess_pipeline
)

from src.features.feature_engineering import (
    feature_engineering
)

from src.model.train_linear_regression import (
    train_linear_regression
)

from src.model.train_random_forest import (
    train_random_forest
)

from src.model.train_gradient_boosting import (
    train_gradient_boosting
)

from src.model.compare_models import (
    compare_models
)


df = load_data()

df = preprocess_pipeline(df)

df = feature_engineering(df)

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

linear_score = train_linear_regression(
    X,
    y
)

rf_score = train_random_forest(
    X,
    y
)

gb_score = train_gradient_boosting(
    X,
    y
)

compare_models(
    linear_score,
    rf_score,
    gb_score
)

print(
    "\nModel Training & Comparison Completed"
)