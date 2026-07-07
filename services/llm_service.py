import streamlit as st
import google.generativeai as genai


def get_model():

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.0-flash-lite"
    )

    return model


def generate_ai_response(prompt):

    model = get_model()

    response = model.generate_content(
        prompt
    )

    return response.text
