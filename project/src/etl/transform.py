import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and normalize the High School Students dataset.

    - Renames columns to snake_case.
    - Converts coded values (e.g., Gender, Ethnicity, ParentalEducation, etc.) to explicit labels.
    - Ensures numeric types are consistent.
    - Adds a normalized record_date column.
    """
    df = df.copy()

    # ---  Renommage clair et normalisé ---
    df.rename(columns={
        "StudentID": "student_id",
        "Age": "age",
        "Gender": "gender",
        "Ethnicity": "ethnicity",
        "ParentalEducation": "parental_education",
        "StudyTimeWeekly": "study_time_weekly",
        "Absences": "absences",
        "Tutoring": "tutoring",
        "ParentalSupport": "parental_support",
        "Extracurricular": "extracurricular",
        "Sports": "sports",
        "Music": "music",
        "Volunteering": "volunteering",
        "GPA": "gpa",
        "GradeClass": "grade_class"
    }, inplace=True)

    # ---  Typage et nettoyage général ---
    numeric_cols = [
        "student_id", "age", "study_time_weekly", "absences", "gpa"
    ]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # --- Décodage des variables catégorielles selon la doc ---
    df["gender"] = df["gender"].replace({
        0: "Male",
        1: "Female"
    })

    df["ethnicity"] = df["ethnicity"].replace({
        0: "Caucasian",
        1: "African American",
        2: "Asian",
        3: "Other"
    })

    df["parental_education"] = df["parental_education"].replace({
        0: "None",
        1: "High School",
        2: "Some College",
        3: "Bachelor's",
        4: "Higher"
    })

    df["parental_support"] = df["parental_support"].replace({
        0: "None",
        1: "Low",
        2: "Moderate",
        3: "High",
        4: "Very High"
    })

    # Variables binaires (0 = No, 1 = Yes)
    binary_cols = ["tutoring", "extracurricular", "sports", "music", "volunteering"]
    for col in binary_cols:
        df[col] = df[col].replace({0: "No", 1: "Yes"})

    # ---  Conversion de GradeClass en lettres selon la doc ---
    df["grade_class"] = df["grade_class"].replace({
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "F"
    })

    # ---  Ajout d’une colonne de date normalisée ---
    df["record_date"] = pd.Timestamp.now().normalize()

    return df

