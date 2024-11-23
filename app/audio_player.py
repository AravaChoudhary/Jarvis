import pyaudio
from io import BytesIO

def play_audio(audio_data):
    """Play the audio data in real-time."""
    p = pyaudio.PyAudio()
  
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    output=True)
    
    stream.write(audio_data)
    stream.stop_stream()
    stream.close()
    p.terminate()