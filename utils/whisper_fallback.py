import whisper
from pytube import YouTube
import os
import uuid

model = whisper.load_model("base")

def transcribe_audio_from_youtube(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        temp_filename = f"temp_audio_{uuid.uuid4()}.mp4"
        audio_stream.download(filename=temp_filename)

        result = model.transcribe(temp_filename)
        os.remove(temp_filename)

        return result["text"]
    except Exception as e:
        return f"Whisper transcription error: {str(e)}"
