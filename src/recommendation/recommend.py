import pandas as pd
import joblib

from src.data.load_data import load_data

from src.preprocessing.preprocess_pipeline import (
    preprocess_pipeline
)

from src.features.feature_engineering import (
    feature_engineering
)

from src.recommendation.similarity_engine import (
    find_similar_phones
)


def recommend_phones():

    print(
        "\n===== SMARTPHONE RECOMMENDATION SYSTEM =====\n"
    )

    budget = float(
        input(
            "Enter Budget (₹): "
        )
    )

    ram = float(
        input(
            "Enter RAM (GB): "
        )
    )

    storage = float(
        input(
            "Enter Storage (GB): "
        )
    )

    front = float(
        input(
            "Enter Front Camera (MP): "
        )
    )

    back = float(
        input(
            "Enter Back Camera (MP): "
        )
    )

    model = joblib.load(
        "models/best_model.pkl"
    )

    user_data = pd.DataFrame(
        [[
            ram,
            storage,
            front,
            back,
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

    predicted_score = model.predict(
        user_data
    )[0]

    print(
        f"\nPredicted Value Score: {predicted_score:.2f}"
    )

    df = load_data()

    df = preprocess_pipeline(df)

    df = feature_engineering(df)

    recommendations = find_similar_phones(
        df,
        budget,
        ram,
        storage,
        front,
        back
    )

    print(
        "\n===== TOP 5 RECOMMENDED PHONES =====\n"
    )

    for idx, row in recommendations.iterrows():

        print(
            f"""
Brand          : {row['Company Name']}
Model          : {row['Model Name']}
RAM            : {row['RAM']} GB
Storage        : {row['Storage']} GB
Front Camera   : {row['Front Camera']} MP
Back Camera    : {row['Back Camera']} MP
Price          : ₹{row['Price']}
Value Score    : {row['Value_Score']:.2f}

------------------------------------------
"""
        )