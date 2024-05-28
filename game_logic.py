from tts import text_to_speech
from speech_recognition_script import recognize_speech_from_mic
from pronunciation_check import check_pronunciation
import streamlit as st

def speech_therapy_game(word_list):
    score = 0
    for word in word_list:
        st.session_state.current_word = word
        text_to_speech(word)
        attempts = 0
        while attempts < 3:
            user_word = recognize_speech_from_mic()
            if check_pronunciation(word, user_word):
                score += 1
                st.success(f"Correct! The word was '{word}'")
                break
            else:
                attempts += 1
                text_to_speech(word)
                st.error(f"Incorrect. Try again: '{word}'")
    return score

# Test the game logic
if __name__ == "__main__":
    words_to_pronounce = ["apple", "banana", "grape"]
    score = speech_therapy_game(words_to_pronounce)
    print(f"Game Over! Your score is: {score}")
