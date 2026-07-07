import streamlit as st
import google.generativeai as genai


def get_model():
    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    return model


def generate_ai_response(prompt):
    model = get_model()

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 6000
            }
        )

        return response.text

    except Exception as e:
        return f"""
⚠️ AI Service Error

Reason:
{str(e)}

Please try again later.
"""
