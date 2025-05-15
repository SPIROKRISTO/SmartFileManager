# src/main.py

import tkinter as tk
from tkinter import filedialog, messagebox
import os

from src.file_handler import deplacer_et_renommer_fichier, detecter_type_fichier
from src.ocr_utils import extraire_texte_fichier
from src.summarizer import resumer_texte
from src.logger import journaliser_traitement

def lancer_interface():
    def choisir_dossier():
        dossier = filedialog.askdirectory()
        if dossier:
            champ_dossier.delete(0, tk.END)
            champ_dossier.insert(0, dossier)

    def traiter_dossier():
        chemin = champ_dossier.get()
        if not chemin or not os.path.isdir(chemin):
            messagebox.showwarning("Attention", "Veuillez choisir un dossier valide.")
            return

        fichiers = [os.path.join(chemin, f) for f in os.listdir(chemin)
                    if os.path.isfile(os.path.join(chemin, f))]

        if not fichiers:
            messagebox.showinfo("Info", "Aucun fichier trouvé dans ce dossier.")
            return

        for fichier in fichiers:
            texte = extraire_texte_fichier(fichier)
            type_fichier = detecter_type_fichier(fichier)
            resume = resumer_texte(texte, nb_phrases=2)
            nouveau_chemin = deplacer_et_renommer_fichier(fichier, "output")
            journaliser_traitement(fichier, type_fichier, resume, nouveau_chemin)

        messagebox.showinfo("✅ Terminé", "Tous les fichiers ont été traités avec succès.")

    # Interface utilisateur
    fen = tk.Tk()
    fen.title("SmartFileManager - Assistant Documentaire Intelligent")
    fen.geometry("600x300")

    tk.Label(fen, text="Sélectionne un dossier contenant les fichiers à traiter :", font=("Arial", 12)).pack(pady=15)
    champ_dossier = tk.Entry(fen, width=60)
    champ_dossier.pack(pady=5)

    tk.Button(fen, text="📁 Parcourir", command=choisir_dossier).pack(pady=5)
    tk.Button(fen, text="🚀 Lancer le traitement", command=traiter_dossier, bg="green", fg="white").pack(pady=20)

    fen.mainloop()

if __name__ == "__main__":
    lancer_interface()
