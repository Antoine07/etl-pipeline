import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie et normalise le jeu de données étudiant."""
    df = df.copy()

    # Renommage des colonnes
    df.rename(columns={
        "Gender": "gender",
        "Race/Ethnicity": "race_ethnicity",
        "Parental Level of Education": "parental_level_of_education",
        "Lunch": "lunch",
        "Test preparation course": "test_preparation_course",
        "Math score": "math_score",
        "Reading score": "reading_score",
        "Writing score": "writing_score"
    }, inplace=True)

     

    return df
