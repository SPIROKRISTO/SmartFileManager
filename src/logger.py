# src/logger.py

import pandas as pd
import os
from datetime import datetime

def journaliser_traitement(nom_fichier, type_fichier, resume, chemin_final, fichier_log="log_documents.csv"):
    """Ajoute une ligne dans le journal CSV avec les infos du traitement."""

    ligne = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Fichier": os.path.basename(nom_fichier),
        "Type": type_fichier,
        "Résumé": resume.strip().replace("\n", " "),
        "Destination": chemin_final
    }

    # Si le fichier existe, ajouter ; sinon, le créer avec entête
    if os.path.exists(fichier_log):
        df = pd.read_csv(fichier_log)
        df = df.append(ligne, ignore_index=True)
    else:
        df = pd.DataFrame([ligne])

    df.to_csv(fichier_log, index=False, encoding="utf-8")
