from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from preprocessing import preprocess_text
from model import predict_sentiment


app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment prediction using a machine learning model",
    version="1.0.0"
)


class PostRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Text for sentiment prediction"
    )


@app.get("/")
def home():
    return {
        "message": "Sentiment Analysis API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(post: PostRequest):

    try:
        cleaned_text = preprocess_text(post.text)

        if not cleaned_text:
            raise HTTPException(
                status_code=400,
                detail="Text cannot be empty"
            )

        sentiment, confidence = predict_sentiment(cleaned_text)

        return {
            "text": post.text,
            "sentiment": str(sentiment),
            "confidence": round(float(confidence), 2)
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )