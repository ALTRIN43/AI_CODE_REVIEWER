import os
import google.generativeai as genai

# Configure Google AI API (Replace with your actual API Key)
API_KEY = os.getenv("GOOGLE_AI_API_KEY")
genai.configure(api_key=API_KEY)

def generate_fixed_code(original_code, errors):
    prompt = f"""
    Here is a code snippet with errors.
    Fix the errors while keeping the logic the same.
    Return only the corrected code without explanations.

    Errors:
    {errors}

    Original Code:
    {original_code}

    Corrected Code:
    """
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text.strip()
