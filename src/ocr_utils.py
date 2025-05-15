# src/ocr_utils.py

from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

# 🔧 Spécifie ici le chemin vers ton installation de Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extraire_texte_image(image_path):
    """Extrait le texte d'une image avec OCR."""
    try:
        image = Image.open(image_path)
        texte = pytesseract.image_to_string(image, lang='eng')
        return texte
    except Exception as e:
        return f"Erreur OCR image : {e}"

def extraire_texte_pdf(pdf_path):
    """Convertit un PDF en images et extrait le texte de chaque page."""
    try:
        pages = convert_from_path(pdf_path, dpi=200)
        texte_total = ""
        for page in pages:
            texte = pytesseract.image_to_string(page, lang='eng')
            texte_total += texte + "\n\n"
        return texte_total
    except Exception as e:
        return f"Erreur OCR PDF : {e}"

def extraire_texte_fichier(fichier):
    """Choisit la bonne méthode en fonction du type de fichier."""
    extension = os.path.splitext(fichier)[1].lower()
    if extension in [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]:
        return extraire_texte_image(fichier)
    elif extension == ".pdf":
        return extraire_texte_pdf(fichier)
    else:
        return "Format non pris en charge pour l'OCR."
