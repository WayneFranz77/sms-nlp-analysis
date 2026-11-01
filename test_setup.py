import pandas as pd
import nltk
import spacy
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer

print("Pandas:", pd.__version__)

nlp = spacy.load("en_core_web_sm")
print("spaCy model loaded successfully")

print("Environment ready!")
