import pandas as pd
from etl.load import load
import os

def test_load_creates_csv(tmp_path):
    # Create a temporary DataFrame with new column names
    df = pd.DataFrame({
        "first_name": ["Alice", "Bob"],
        "last_name": ["Doe", "Smith"],
        "id": ["alice123", "bob456"],
        "personal_email": ["alice@gmail.com", "bob@gmail.com"],
        "school_email": ["alice@school.com", "bob@school.com"],
        "status": ["done", "done"],
        "registration_date": ["2025-01-01", "2025-01-02"],
        "school": ["SCHOOL 1", "SCHOOL 2"]
    })

    output_file = tmp_path / "output.csv"
    
    # Call the load function
    load(df, str(output_file))
    
    # ---- Checks ----
    
    # File was created
    assert output_file.exists()
    
    # Check that data was correctly written
    df_loaded = pd.read_csv(output_file)
    assert df_loaded.shape == df.shape
    assert list(df_loaded.columns) == list(df.columns)
    assert df_loaded['first_name'].iloc[1] == "Bob"
    assert df_loaded['school'].iloc[0] == "SCHOOL 1"
