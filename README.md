# 🎬 YouTube Video Summarizer & Sinhala Translator

A simple FastAPI project that:
- Extracts the transcript from a YouTube video.
- Summarizes the video content using **Google Gemini**.
- Translates the summary into **Sinhala** using **Google Translate**.
- Returns both English and Sinhala summaries via an API endpoint.
- Download the summary pdf
- Ask questions from the summary

---

## 📁 Project Structure

```
youtube-summary-translator/
│
├── main.py 
├── requirements.txt 
├── .env 
├── README.md 
│
└── utils/
        transcript.py # YouTube transcript extraction
        summarizer.py # Summarization with Gemini API
        translator.py # English → Sinhala translation
```

### To run

```
uvicorn main:app --reload

```
