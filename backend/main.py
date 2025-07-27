from fastapi import FastAPI, Query
from utils.transcript import get_transcript
from utils.summarizer import summarize_text
from utils.translator import translate_to_sinhala
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware



load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "YouTube Summarizer API running!"}

@app.get("/summarize/")
def summarize_video(url: str = Query(..., description="YouTube video URL")):
    transcript = get_transcript(url)
    summary = summarize_text(transcript)
    sinhala_summary = translate_to_sinhala(summary)
    return {
        "transcript_excerpt": transcript[:300] + "...",
        "summary_en": summary,
        "summary_si": sinhala_summary
        
    }
