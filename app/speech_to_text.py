import pyaudio
import requests
import json

def record_audio():
    """Record audio from the microphone and return as byte stream."""
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)
    
    print("Recording...")
    frames = []
    for i in range(0, int(16000 / 1024 * 5)):
        data = stream.read(1024)
        frames.append(data)
    
    print("Recording finished")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return b''.join(frames)

def audio_to_text(audio_data):
    """Send recorded audio to Deepgram API for transcription."""
    url = "https://api.deepgram.com/v1/listen"
    headers = {
        "Authorization": "Bearer YOUR_DEEPGRAM_API_KEY"
    }
    
    response = requests.post(url, headers=headers, data=audio_data)
    
    if response.status_code == 200:
        transcript = json.loads(response.text)['results']['channels'][0]['alternatives'][0]['transcript']
        return transcript
    else:
        return "Sorry, I couldn't understand that."