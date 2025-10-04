import pandas as pd
from src.etl.extract import extract as extract_csv

def test_extract_csv(tmp_path):
    # --- Arrange ---
    test_csv = tmp_path / "data.csv"
    data = "StudentID,Age,Gender,Ethnicity\n1001,17,1,0\n1002,18,0,2"
    test_csv.write_text(data)

    # --- Act ---
    df = extract_csv(test_csv)

    # --- Assert ---
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 4)
    assert list(df.columns) == ["StudentID", "Age", "Gender", "Ethnicity"]
