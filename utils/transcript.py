from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    match = re.search(r"(?<=v=)[^&#]+", url) or re.search(r"(?<=youtu.be/)[^&#]+", url)
    return match.group(0) if match else None

def get_transcript(url):
    video_id = extract_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([segment['text'] for segment in transcript])
        return full_text
    except Exception as e:
        return f"Transcript not available: {str(e)}"
