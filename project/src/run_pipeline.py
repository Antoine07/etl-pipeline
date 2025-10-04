import pandas as pd
from etl.transform import clean_data
from etl.load import load

# Charger le CSV brut
df_raw = pd.read_csv("./data/Student_performance_data _raw.csv")

# Nettoyer les données
df_clean = clean_data(df_raw)

# Enregistrer le CSV nettoyé
load(df_clean, "./data/clean_students.csv")
