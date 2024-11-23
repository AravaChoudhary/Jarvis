import requests
from io import BytesIO

def text_to_speech(response_text):
    """Convert text to speech using Deepgram TTS API."""
    url = "https://api.deepgram.com/v1/synthesize"
    headers = {
        "Authorization": "Bearer YOUR_DEEPGRAM_API_KEY"
    }
    data = {
        "text": response_text,
        "voice": "en_us_male",
        "rate": 1.0,
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        return None