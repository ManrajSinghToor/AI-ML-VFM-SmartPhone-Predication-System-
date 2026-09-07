import pandas as pd

def load_data(path="dataset/smartphones.csv"):

    df = pd.read_csv(path)

    print("\nDataset Loaded Successfully")
    print("Shape:", df.shape)

    return df