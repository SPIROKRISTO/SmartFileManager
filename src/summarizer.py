# src/summarizer.py

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # Tu peux aussi essayer LexRank ou Luhn

def resumer_texte(texte, nb_phrases=3):
    """Résume le texte donné en un nombre de phrases."""
    try:
        parser = PlaintextParser.from_string(texte, Tokenizer("french"))  # ou "english"
        summarizer = LsaSummarizer()
        resume = summarizer(parser.document, nb_phrases)
        texte_resume = " ".join([str(phrase) for phrase in resume])
        return texte_resume
    except Exception as e:
        return f"Erreur dans le résumé : {e}"
