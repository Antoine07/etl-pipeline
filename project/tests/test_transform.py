import pandas as pd

from src.etl.transform import clean_data

def test_clean_data_basic():
    # --- Arrange ---
    raw_data = {
        "StudentID": [1001, 1002],
        "Age": [17, 18],
        "Gender": [1, 0],
        "Ethnicity": [0, 2],
        "ParentalEducation": [2, 4],
        "StudyTimeWeekly": [10, 15],
        "Absences": [5, 2],
        "Tutoring": [1, 0],
        "ParentalSupport": [3, 2],
        "Extracurricular": [1, 0],
        "Sports": [0, 1],
        "Music": [0, 1],
        "Volunteering": [1, 0],
        "GPA": [3.8, 2.7],
        "GradeClass": [0, 2]
    }
    
    df = pd.DataFrame(raw_data)

    # --- Act ---
    cleaned = clean_data(df)

    # --- Assert ---
    assert "gender" in cleaned.columns

    assert cleaned["gender"].tolist() == ["Female", "Male"]
    assert cleaned["ethnicity"].tolist() == ["Caucasian", "Asian"]
    assert cleaned["grade_class"].tolist() == ["A", "C"]

    # Vérifie que la colonne de date a bien été ajoutée
    assert "record_date" in cleaned.columns
    