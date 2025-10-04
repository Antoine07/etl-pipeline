import pandas as pd
from etl.extract import extract

def test_extract_returns_dataframe(tmp_path):
    # Create a small temporary CSV for testing with new column names
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        "first_name,last_name,id,personal_email,school_email,status,registration_date,school\n"
        "Alice,Doe,alice123,alice@gmail.com,alice@school.com,done,2025-01-01,SCHOOL 1\n"
        "Bob,Smith,bob456,bob@gmail.com,bob@school.com,done,2025-01-02,SCHOOL 2"
    )

    df = extract(str(csv_file))
    
    # ---- Checks ----
    
    # DataFrame type
    assert isinstance(df, pd.DataFrame)
    
    # Correct shape
    assert df.shape == (2, 8)  # 2 rows, 8 columns
    
    # Correct columns
    expected_columns = [
        "first_name", "last_name", "id",
        "personal_email", "school_email",
        "status", "registration_date", "school"
    ]
    assert list(df.columns) == expected_columns
    
    # Check first row values
    assert df['first_name'].iloc[0] == "Alice"
    assert df['school'].iloc[1] == "SCHOOL 2"
