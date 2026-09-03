from fastapi import FastAPI
from pydantic import BaseModel

from preprocessing import preprocess_text
from model import predict_sentiment


app = FastAPI(
    title="Sentiment Analysis API",
    description="FastAPI service for sentiment prediction",
    version="1.0.0"
)


class PostRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Sentiment Analysis API is running"
    }


@app.post("/predict")
def predict(post: PostRequest):

    cleaned_text = preprocess_text(post.text)

    sentiment, confidence = predict_sentiment(cleaned_text)

    return {
        "text": post.text,
        "sentiment": sentiment,
        "confidence": round(float(confidence), 2)
    }