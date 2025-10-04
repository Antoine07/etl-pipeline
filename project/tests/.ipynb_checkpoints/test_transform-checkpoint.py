import pandas as pd
from etl.transform import clean_data

def test_clean_data_on_raw_students():
    # Load raw CSV
    df_raw = pd.read_csv("data/raw_students.csv")
    
    # Apply cleaning
    df_clean = clean_data(df_raw)
    
    # ---- Main checks ----
    
    # 1️⃣ First and last names: strip and title-case
    assert all(df_clean['first_name'].str[0].str.isupper())
    assert all(df_clean['first_name'].str.strip() == df_clean['first_name'])
    assert all(df_clean['last_name'].str[0].str.isupper())

    # 2️⃣ Emails: lowercase and valid
    for col in ['personal_email', 'school_email']:
        # Check lowercase
        assert df_clean[col].str.lower().eq(df_clean[col]).all()
        # Check that all non-missing emails contain '@'
        assert df_clean[col].dropna().str.contains("@").all()
    
    # 3️⃣ Status: all normalized to 'done'
    assert all(df_clean['status'] == "done")
    
    # 4️⃣ Registration dates: valid datetime or NaT
    assert pd.api.types.is_datetime64_any_dtype(df_clean['registration_date'])
    
    # 5️⃣ School names: uppercase, no underscores or hyphens
    assert all(df_clean['school'].str.isupper())
    assert not df_clean['school'].str.contains("_|-").any()
    
    # 6️⃣ Number of rows unchanged
    assert len(df_clean) == len(df_raw)
