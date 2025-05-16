import google.generativeai as genai
import os
from app.core.config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel("gemini-2.0-flash")

def generate_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No response from Gemini."
    except Exception as e:
        print("Gemini API Error:", e)
        return "Error generating response."

