import matplotlib.pyplot as plt
import joblib


def compare_models(
        linear_score,
        rf_score,
        gb_score
):

    scores = {

        "Linear Regression": linear_score,

        "Random Forest": rf_score,

        "Gradient Boosting": gb_score

    }

    print("\n===== MODEL COMPARISON =====")

    for model, score in scores.items():

        print(
            f"{model} : {score:.4f}"
        )

    best_model_name = max(
        scores,
        key=scores.get
    )

    print(
        f"\nBest Model : {best_model_name}"
    )

    if best_model_name == "Linear Regression":

        best_model = joblib.load(
            "models/linear_regression.pkl"
        )

    elif best_model_name == "Random Forest":

        best_model = joblib.load(
            "models/random_forest.pkl"
        )

    else:

        best_model = joblib.load(
            "models/gradient_boosting.pkl"
        )

    joblib.dump(
        best_model,
        "models/best_model.pkl"
    )

    plt.figure(figsize=(8,5))

    plt.bar(
        scores.keys(),
        scores.values()
    )

    plt.title(
        "Model Comparison"
    )

    plt.ylabel(
        "R2 Score"
    )

    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/model_comparison.png"
    )

    plt.close()

    print(
        "\nBest Model Saved Successfully"
    )