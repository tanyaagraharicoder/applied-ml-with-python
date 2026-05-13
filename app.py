import streamlit as st
import pandas as pd
import numpy as np
import string
import nltk
import pickle

from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Emotion labels
emotion_map = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

# Text Cleaning Function
def clean_text(text):

    # lowercase
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # remove numbers
    text = ''.join([i for i in text if not i.isdigit()])

    # remove emojis/non-ascii
    text = ''.join([i for i in text if i.isascii()])

    # remove stopwords
    words = text.split()

    cleaned_words = []

    for word in words:
        if word not in stop_words:
            cleaned_words.append(word)

    return " ".join(cleaned_words)

# Streamlit UI
st.set_page_config(
    page_title="Emotion Detector",
    page_icon="😊",
    layout="centered"
)

st.title("😊 NLP Emotion Detection App")

st.write("Enter a sentence and detect emotion")

# Input box
user_input = st.text_area("Enter Text")

# Prediction button
if st.button("Predict Emotion"):

    if user_input.strip() != "":

        cleaned_text = clean_text(user_input)

        transformed_text = vectorizer.transform([cleaned_text])

        prediction = model.predict(transformed_text)[0]

        emotion = emotion_map[prediction]

        st.success(f"Predicted Emotion: {emotion}")

    else:
        st.warning("Please enter some text")