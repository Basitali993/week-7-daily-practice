import re


def preprocess_text(text):

    text = text.strip()

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()