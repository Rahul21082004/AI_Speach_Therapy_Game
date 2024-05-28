import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Test the TTS functionality
if __name__ == "__main__":
    text_to_speech("Hello, please pronounce the word 'apple'.")
