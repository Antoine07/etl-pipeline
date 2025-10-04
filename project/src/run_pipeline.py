import pandas as pd
from etl.transform import clean_data
from etl.load import load
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # remonte de src/ vers project/
DATA_DIR = BASE_DIR / "data"

raw_path = DATA_DIR / "Student_performance_data _raw.csv"
clean_path = DATA_DIR / "clean_students.csv"

# Charger le CSV brut
df_raw = pd.read_csv(raw_path)

# Nettoyer les données
df_clean = clean_data(df_raw)

# Enregistrer le CSV nettoyé
load(df_clean, str(clean_path ) ) # Sauvegarde le DataFrame nettoyé en CSV
