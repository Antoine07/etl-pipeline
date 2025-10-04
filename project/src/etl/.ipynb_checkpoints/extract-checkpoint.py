import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    """Charge le CSV brut en DataFrame."""
    return pd.read_csv(filepath, sep=",")
