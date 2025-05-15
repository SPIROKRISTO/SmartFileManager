# src/file_handler.py

import os
import shutil
from datetime import datetime

def detecter_type_fichier(fichier):
    """Retourne le type du fichier : image, pdf, texte, autre."""
    extension = os.path.splitext(fichier)[1].lower()
    if extension in [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]:
        return "images"
    elif extension == ".pdf":
        return "pdf"
    elif extension in [".txt", ".docx"]:
        return "textes"
    else:
        return "non_reconnus"

def renommer_fichier(fichier, prefixe="document"):
    """Renomme le fichier avec un préfixe et un horodatage."""
    dossier, nom = os.path.split(fichier)
    ext = os.path.splitext(nom)[1]
    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    nouveau_nom = f"{prefixe}_{horodatage}{ext}"
    return os.path.join(dossier, nouveau_nom)

def deplacer_et_renommer_fichier(fichier, dossier_sortie):
    """Détecte, renomme, déplace et retourne le nouveau chemin."""
    type_fichier = detecter_type_fichier(fichier)
    dossier_cible = os.path.join(dossier_sortie, type_fichier)

    if not os.path.exists(dossier_cible):
        os.makedirs(dossier_cible)

    nouveau_nom = renommer_fichier(fichier, prefixe=type_fichier)
    chemin_destination = os.path.join(dossier_cible, os.path.basename(nouveau_nom))

    shutil.copy2(fichier, chemin_destination)  # ou shutil.move si tu veux déplacer
    return chemin_destination
