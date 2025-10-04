def load(df, filepath: str):
    """Sauvegarde le DataFrame nettoyé en CSV."""
    df.to_csv(filepath, index=False)
