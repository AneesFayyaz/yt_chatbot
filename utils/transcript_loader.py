from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url: str) -> str:
    video_id = video_url.split("v=")[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t["text"] for t in transcript])
    return text
