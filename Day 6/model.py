import joblib

MODEL_PATH = "sentiment_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Model loading error: {e}")


def predict_sentiment(text):

    if model is None:
        raise RuntimeError("Sentiment model is not available")

    prediction = model.predict([text])[0]

    confidence = 0.0

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([text])[0]
        confidence = max(probabilities)

    return prediction, confidence