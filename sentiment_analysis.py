import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import nltk
import re

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')
from nltk.corpus import stopwords

# Sample dataset (expanded for better learning)
data = {
    "text": [
        "I love this product!",
        "This is the worst service ever.",
        "It's okay, not bad.",
        "Absolutely fantastic experience.",
        "I hate it!",
        "Could be better.",
        "Horrible customer support.",
        "Excellent! I'm very satisfied.",
        "This is the best I’ve used.",
        "Very bad experience.",
        "Not good, not bad, just average.",
        "Wonderful item, works like a charm!",
        "Disappointing and frustrating.",
        "Neutral experience, nothing special.",
        "I'm very happy with the service.",
        "Worst product ever.",
        "Amazing quality and service!",
        "Terrible. Would not recommend.",
        "It’s fine, nothing great.",
        "Just okay."
    ],
    "sentiment": [
        "positive", "negative", "neutral", "positive", "negative", "neutral",
        "negative", "positive", "positive", "negative", "neutral", "positive",
        "negative", "neutral", "positive", "negative", "positive", "negative",
        "neutral", "neutral"
    ]
}

# Load data
df = pd.DataFrame(data)

# Text preprocessing
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return ' '.join(filtered)

df['clean_text'] = df['text'].apply(preprocess)

# Split dataset with stratification
X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'],
    df['sentiment'],
    test_size=0.3,
    random_state=42,
    stratify=df['sentiment']
)

# Vectorize text
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))
