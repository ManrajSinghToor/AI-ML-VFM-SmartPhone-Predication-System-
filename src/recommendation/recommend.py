import pandas as pd
import joblib

from src.visualization.recommendation_graphs import (
    generate_recommendation_graphs
)

def recommend_phones():

    print("\n===== Smartphone Recommender =====\n")

    budget = float(
        input("Enter Budget (₹): ")
    )

    ram = float(
        input("Enter RAM (GB): ")
    )

    storage = float(
        input("Enter Storage (GB): ")
    )

    front_camera = float(
        input("Enter Front Camera (MP): ")
    )

    back_camera = float(
        input("Enter Back Camera (MP): ")
    )

    # Load dataset
    df = pd.read_csv(
        "dataset/featured_data.csv"
    )

    # Load trained model
    model = joblib.load(
        "models/best_model.pkl"
    )
    scaler = joblib.load(
        "models/scaler.pkl"
    )

    # Predict user's expected value score
    user_data = pd.DataFrame(
        [[
            ram,
            storage,
            front_camera,
            back_camera,
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
    user_data_scaled = scaler.transform(
        user_data
    )
    predicted_score = model.predict(
        user_data_scaled
    )[0]

    print(
        f"\nPredicted Value Score: {predicted_score:.2f}"
    )

    # Budget Filter
    filtered = df[
        df["Price"] <= budget
    ].copy()

    if len(filtered) == 0:

        print(
            "\nNo phones found within budget."
        )

        return

    # Similarity / Match Score
    filtered["Match_Score"] = (

        abs(filtered["RAM"] - ram)

        +

        abs(filtered["Storage"] - storage)

        +

        abs(
            filtered["Front Camera"]
            - front_camera
        )

        +

        abs(
            filtered["Back Camera"]
            - back_camera
        )

    )

    # Sort:
    # Closest match first
    # Then highest Value Score

    recommendations = filtered.sort_values(
        by=[
            "Match_Score",
            "Value_Score"
        ],
        ascending=[
            True,
            False
        ]
    ).head(5)

    print(
        "\n===== Top 5 Recommended Phones =====\n"
    )

    print(
        recommendations[
            [
                "Company Name",
                "Model Name",
                "RAM",
                "Storage",
                "Front Camera",
                "Back Camera",
                "Price",
                "Value_Score"
            ]
        ]
    )

    generate_recommendation_graphs(
        recommendations
    )

    print(
        "\nRecommendation Graphs Saved"
    )