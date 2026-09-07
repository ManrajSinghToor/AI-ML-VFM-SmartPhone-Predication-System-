from src.preprocessing.clean_data import clean_data

def preprocess_pipeline(df):

    df = clean_data(df)

    return df