from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib


texts = [
    "I love this product",
    "This is an excellent service",
    "The product is amazing",
    "I really like this application",
    "This is a great experience",
    "The service is good",

    "I hate this product",
    "This service is terrible",
    "The product is awful",
    "I dislike this application",
    "This is a bad experience",
    "The service is poor",

    "The product is available",
    "The application is running",
    "The service is currently active",
    "The product was delivered today",
    "The application has a new version",
    "The service is available"
]

labels = [
    "positive",
    "positive",
    "positive",
    "positive",
    "positive",
    "positive",

    "negative",
    "negative",
    "negative",
    "negative",
    "negative",
    "negative",

    "neutral",
    "neutral",
    "neutral",
    "neutral",
    "neutral",
    "neutral"
]


model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

model.fit(texts, labels)

joblib.dump(model, "sentiment_model.pkl")

print("Sentiment model trained and saved successfully.")