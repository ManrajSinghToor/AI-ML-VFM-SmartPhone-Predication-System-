import matplotlib.pyplot as plt


def generate_recommendation_graphs(recommended):

    # Price Comparison

    plt.figure(figsize=(10, 5))

    plt.bar(
        recommended["Model Name"],
        recommended["Price"]
    )

    plt.title("Recommended Phones Price Comparison")

    plt.xlabel("Phone")

    plt.ylabel("Price (₹)")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/recommended_price_comparison.png"
    )

    plt.close()


    # Value Score Comparison

    plt.figure(figsize=(10, 5))

    plt.bar(
        recommended["Model Name"],
        recommended["Value_Score"]
    )

    plt.title("Recommended Phones Value Score Comparison")

    plt.xlabel("Phone")

    plt.ylabel("Value Score")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/recommended_value_score.png"
    )

    plt.close()


    # RAM Comparison

    plt.figure(figsize=(10, 5))

    plt.bar(
        recommended["Model Name"],
        recommended["RAM"]
    )

    plt.title("Recommended Phones RAM Comparison")

    plt.xlabel("Phone")

    plt.ylabel("RAM (GB)")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/recommended_ram_comparison.png"
    )

    plt.close()

    print("\nRecommendation Graphs Saved")