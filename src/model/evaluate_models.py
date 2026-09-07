from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

import numpy as np


def evaluate_model(
        y_test,
        predictions
):

    r2 = r2_score(
        y_test,
        predictions
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    print("\n===== MODEL EVALUATION =====")

    print(
        f"R2 Score : {r2:.4f}"
    )

    print(
        f"MAE : {mae:.4f}"
    )

    print(
        f"RMSE : {rmse:.4f}"
    )