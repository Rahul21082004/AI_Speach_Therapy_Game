import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    try:
        response = recognizer.recognize_google(audio, show_all=False)
        return response
    except sr.RequestError:
        return "API unavailable"
    except sr.UnknownValueError:
        return "Unable to recognize speech"

# Test the speech recognition functionality
if __name__ == "__main__":
    print("Please say something")
    recognized_text = recognize_speech_from_mic()
    print("You said: " + recognized_text)
