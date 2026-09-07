import matplotlib.pyplot as plt

def generate_graphs(df):
    print("FUNCTION CALLED")

def generate_graphs(df):

    print("\nGenerating Graphs...")

    plt.figure(figsize=(8,5))

    plt.hist(
        df["Price"],
        bins=30
    )

    plt.title("Price Distribution")

    plt.xlabel("Price")

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/price_distribution.png"
    )

    plt.close()

    plt.figure(figsize=(8,5))

    plt.scatter(
        df["RAM"],
        df["Price"]
    )

    plt.title(
        "RAM vs Price"
    )

    plt.xlabel(
        "RAM"
    )

    plt.ylabel(
        "Price"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/ram_vs_price.png"
    )

    plt.close()

    corr = df[
        [
            "RAM",
            "Storage",
            "Front Camera",
            "Back Camera",
            "Price",
            "Value_Score"
        ]
    ].corr()

    plt.figure(figsize=(8,6))

    plt.imshow(corr)

    plt.colorbar()

    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=45
    )

    plt.yticks(
        range(len(corr.columns)),
        corr.columns
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/correlation_heatmap.png"
    )
    plt.figure(figsize=(8,5))

    plt.scatter(
        df["Storage"],
        df["Price"]
    )

    plt.title(
        "Storage vs Price"
    )

    plt.xlabel(
        "Storage"
    )

    plt.ylabel(
        "Price"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/graphs/storage_vs_price.png"
    )
    plt.close()

    print("Graphs Saved")