from fastapi import FastAPI

app = FastAPI(
    title="Sentiment Analysis API",
    description="Basic FastAPI application for Week 7",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Sentiment API is running"
    }


@app.get("/about")
def about():
    return {
        "project": "Sentiment Analysis API",
        "week": "Week 7",
        "day": "Day 2"
    }


@app.post("/test")
def test_api():
    return {
        "message": "POST request received successfully"
    }