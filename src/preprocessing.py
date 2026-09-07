from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):

    encoder = LabelEncoder()

    df["brand"] = encoder.fit_transform(df["brand"])

    scaler = StandardScaler()

    features = [
        "price",
        "ram",
        "storage",
        "battery",
        "camera"
    ]

    X = df[features]

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler