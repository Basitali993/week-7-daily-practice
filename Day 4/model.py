import joblib

MODEL_PATH = "sentiment_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_sentiment(text):
    prediction = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]

    confidence = max(probabilities)

    return prediction, confidence