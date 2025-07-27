from youtube_transcript_api import YouTubeTranscriptApi
import re
from .whisper_fallback import transcribe_audio_from_youtube

import re

def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    # Handle both short and long YouTube URLs
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")


def get_transcript(url):
    video_id = extract_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([segment['text'] for segment in transcript])
        return full_text
    except Exception:
        # Fallback to Whisper
        return transcribe_audio_from_youtube(url)
