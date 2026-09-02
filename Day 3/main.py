from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Sentiment Prediction API",
    description="API for predicting sentiment from text",
    version="1.0.0"
)


class PostRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Sentiment Prediction API is running"
    }


@app.post("/predict")
def predict_sentiment(post: PostRequest):
    text = post.text.lower()

    positive_words = [
        "good",
        "great",
        "excellent",
        "amazing",
        "love",
        "like",
        "happy",
        "best"
    ]

    negative_words = [
        "bad",
        "terrible",
        "hate",
        "worst",
        "poor",
        "awful",
        "sad",
        "disappointing"
    ]

    positive_count = sum(word in text for word in positive_words)
    negative_count = sum(word in text for word in negative_words)

    if positive_count > negative_count:
        sentiment = "positive"
    elif negative_count > positive_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "text": post.text,
        "sentiment": sentiment
    }