import re


def preprocess_text(text):
    text = text.lower()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text