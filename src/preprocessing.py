import pandas as pd

def load_dataset(path):
    """
    Load the transaction dataset from a CSV file.
    Assumes dataset is one-hot encoded.
    """
    try:
        df = pd.read_csv(path, index_col=0)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def inspect_data(df, num_rows=5):
    """
    Quick preview of the data.
    """
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    return df.head(num_rows)
