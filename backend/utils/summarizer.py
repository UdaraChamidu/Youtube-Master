import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_text(transcript):
    if transcript.startswith("Transcript not available"):
        return transcript

    prompt = f"Summarize the following YouTube video transcript:\n\n{transcript}"

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini summarization error: {str(e)}"
