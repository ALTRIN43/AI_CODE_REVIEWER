import google.generativeai as genai

# Configure Google AI API (Replace with your actual API Key)
genai.configure(api_key="Replace with your api")

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
