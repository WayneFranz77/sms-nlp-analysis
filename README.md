# SMS NLP Analysis

## Overview

This project explores a large collection of SMS messages using Natural Language Processing (NLP) techniques. The goal is to transform unstructured text into meaningful insights through preprocessing, visualization, sentiment analysis, linguistic analysis, named entity recognition, and text similarity analysis.

The project uses the NUS SMS Corpus and demonstrates a complete NLP workflow from raw text to actionable insights.

---

## Objectives

- Explore SMS communication patterns
- Clean and preprocess text data
- Analyze message lengths and distributions
- Identify commonly used words
- Visualize language patterns
- Perform sentiment analysis
- Extract named entities
- Analyze grammatical structure
- Measure text similarity using vectorization techniques

---

## Dataset

This project uses the **NUS SMS Corpus**, a large collection of SMS messages originating from multiple countries.

### Dataset Summary

| Metric | Value |
|----------|---------:|
| Total Messages | 48,598 |
| Valid Messages After Cleaning | 48,595 |
| Countries Represented | Multiple |
| Primary Language | English |
| Data Type | SMS Messages |

Dataset columns:

- ID
- Message
- Length
- Country
- Date

---

## Technologies Used

### Python Libraries

- pandas
- numpy
- matplotlib
- seaborn
- nltk
- spaCy
- scikit-learn
- wordcloud
- textblob
- jupyter

### NLP Techniques

- Text Cleaning
- Tokenization
- Stopword Removal
- Lemmatization
- Word Frequency Analysis
- Word Cloud Visualization
- Sentiment Analysis
- Named Entity Recognition (NER)
- Part-of-Speech (POS) Tagging
- TF-IDF Vectorization
- Cosine Similarity Analysis

---

## Project Structure

```text
sms-nlp-analysis/
│
├── data/
│   └── clean_nus_sms.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── sentiment.py
│   ├── topic_modeling.py
│   ├── ner.py
│   └── visualization.py
│
├── images/
│
├── LICENSE
├── README.md
├── requirements.txt
└── report.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/WayneFranz77/sms-nlp-analysis.git

cd sms-nlp-analysis
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required NLP Resources

### Download NLTK Resources

```python
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("vader_lexicon")
```

### Install spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

---

## Analysis Workflow

### 1. Data Cleaning

The dataset was cleaned by:

- Removing missing messages
- Removing unnecessary columns
- Converting message lengths to numeric format
- Standardizing data for analysis

---

### 2. Text Preprocessing

A reusable preprocessing pipeline was developed to:

- Convert text to lowercase
- Remove URLs
- Remove punctuation
- Remove numerical values
- Tokenize text
- Remove stopwords
- Apply lemmatization

---

### 3. Exploratory Analysis

Analysis included:

- Dataset structure
- Missing values
- Message length distribution
- Country distribution

---

### 4. Word Frequency Analysis

The most frequently occurring words were extracted and visualized.

Common words included:

- haha
- hey
- ok
- today
- time
- going
- think

These results suggest that SMS communication is largely conversational and focused on social interaction and planning.

---

### 5. Word Cloud Visualization

A word cloud was generated to visually represent frequently occurring words throughout the SMS corpus.

The visualization highlighted:

- Informal language
- Social interactions
- Time-related discussions
- Planning and coordination

---

### 6. Sentiment Analysis

Sentiment was analyzed using NLTK's VADER sentiment analyzer.

#### Results

| Sentiment | Messages | Percentage |
|------------|---------:|-----------:|
| Positive | 21,488 | 44.22% |
| Neutral | 21,426 | 44.09% |
| Negative | 5,681 | 11.69% |

#### Key Insight

Over 88% of messages were classified as either positive or neutral, suggesting that SMS messaging is primarily used for casual and friendly communication.

---

### 7. Named Entity Recognition (NER)

Named Entity Recognition was performed using spaCy.

Entity categories identified included:

- Dates
- Times
- Numbers
- Ordinals
- People
- Organizations

#### Findings

The model performed well on conventional entities such as:

- today
- tomorrow
- tonight

However, some SMS slang and abbreviations were incorrectly classified, highlighting challenges associated with applying formal NLP models to informal SMS text.

---

### 8. Part-of-Speech (POS) Tagging

POS tagging was used to analyze the grammatical structure of messages.

#### Most Common POS Categories

| POS Tag | Count |
|----------|---------:|
| PUNCT | 10,120 |
| NOUN | 9,973 |
| VERB | 8,716 |
| PRON | 6,665 |
| PROPN | 6,227 |

#### Key Insight

SMS communication is highly conversational and action-oriented, with heavy use of nouns, verbs, pronouns, and proper nouns.

---

### 9. Text Similarity Analysis

TF-IDF vectorization and cosine similarity were used to compare messages.

Applications include:

- Duplicate message detection
- Message clustering
- Search systems
- Recommendation systems

This demonstrates how text can be transformed into numerical representations suitable for machine learning.

---

## Key Findings

### Communication Style

SMS communication appears primarily informal, conversational, and social.

### Sentiment

The majority of messages are positive or neutral.

### Language Patterns

Frequent use of:

- Informal expressions
- Abbreviations
- Pronouns
- Action-oriented language

### Regional Characteristics

The corpus contains region-specific expressions such as:

- lor
- leh
- liao

reflecting the Singaporean origins of the NUS SMS Corpus.

---

## Limitations

This analysis has several limitations:

- SMS language contains abbreviations and slang that may reduce NLP accuracy.
- Sentiment analysis may struggle with sarcasm or contextual meaning.
- Named Entity Recognition models are trained primarily on formal written text.
- Some advanced analyses were conducted on subsets of the dataset for efficiency.

---

## Future Improvements

Potential future enhancements include:

- Topic Modeling (LDA)
- Word2Vec Embeddings
- SMS Classification
- Message Clustering
- Deep Learning Sentiment Analysis
- Interactive Dashboard Development
- Real-Time Message Analysis Pipeline

---

## Learning Outcomes

This project demonstrates practical experience with:

- Natural Language Processing
- Exploratory Data Analysis
- Text Preprocessing
- Statistical Analysis
- Data Visualization
- Sentiment Analysis
- Vector Space Models
- Similarity Metrics

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

## Author

**Wayne Franz**

NLP Portfolio Project completed as part of ongoing studies in Artificial Intelligence, Machine Learning, and Natural Language Processing.