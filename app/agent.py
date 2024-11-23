from .speech_to_text import record_audio, audio_to_text
from .nlp import get_openai_response
from .text_to_speech import text_to_speech
from .audio_player import play_audio

def start_voice_agent():
    print("Starting the voice agent...")
   
    audio_data = record_audio()
    
    text_input = audio_to_text(audio_data)
    print(f"User said: {text_input}")
    
    response_text = get_openai_response(text_input)
    print(f"Response: {response_text}")
    
    audio_response = text_to_speech(response_text)
    
    if audio_response:
        play_audio(audio_response.read())

if __name__ == "__main__":
    start_voice_agent()