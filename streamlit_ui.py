import streamlit as st
from app.agent import start_voice_agent

def main():
    st.title("Voice Agent")
    
    if st.button("Start Voice Interaction"):
        st.write("Recording your voice...")
        start_voice_agent()
        st.write("Response played back to you!")

if __name__ == "__main__":
    main()