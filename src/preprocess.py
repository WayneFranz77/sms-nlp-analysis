"""
preprocess.py

Reusable text preprocessing functions for SMS NLP analysis.
"""

import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()


def clean_text(text):
    """
    Basic text cleaning.
    """

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize(text):
    """
    Tokenize text into words.
    """

    return word_tokenize(text)


def remove_stopwords(tokens):
    """
    Remove common stop words.
    """

    return [token for token in tokens if token not in STOP_WORDS]


def lemmatize(tokens):
    """
    Lemmatize tokens.
    """

    return [LEMMATIZER.lemmatize(token) for token in tokens]


def preprocess_text(text):
    """
    Full preprocessing pipeline.
    """

    text = clean_text(text)

    tokens = tokenize(text)

    tokens = remove_stopwords(tokens)

    tokens = lemmatize(tokens)

    return tokens


if __name__ == "__main__":

    sample = "Hey Wayne! Meet me at https://test.com tomorrow at 10am."

    print("Original:")
    print(sample)

    print("\nProcessed:")
    print(preprocess_text(sample))
