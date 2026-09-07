def find_similar_phones(
        df,
        budget,
        ram,
        storage,
        front,
        back
):

    phones = df.copy()

    phones = phones[
        phones["Price"] <= budget * 1.20
    ]

    phones["Similarity_Score"] = (

        abs(phones["RAM"] - ram)

        +

        abs(
            phones["Storage"] - storage
        )

        +

        abs(
            phones["Front Camera"] - front
        )

        +

        abs(
            phones["Back Camera"] - back
        )

        +

        (
            abs(
                phones["Price"] - budget
            ) / 1000
        )

    )

    phones = phones.sort_values(
        by="Similarity_Score"
    )

    return phones.head(5)