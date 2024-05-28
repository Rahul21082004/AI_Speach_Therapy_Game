import streamlit as st
from game_logic import speech_therapy_game

# Initialize session state for score and level
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'level' not in st.session_state:
    st.session_state.level = 1

# Set up the Streamlit app
st.title("AI Speech Therapy Game")

# List of words for different levels
word_levels = {
    1: ["apple", "banana", "grape"],
    2: ["elephant", "giraffe", "dolphin"],
    3: ["orchestra", "philosophy", "substantial"],
    4: ["mitochondria", "biochemistry", "electromagnetic"],
    5: ["photosynthesis", "quantum", "astrophysics"],
    6: ["supercalifragilisticexpialidocious", "pseudopseudohypoparathyroidism", "floccinaucinihilipilification"],
    7: ["onomatopoeia", "antidisestablishmentarianism", "honorificabilitudinitatibus"],
    8: ["hippopotomonstrosesquipedaliophobia", "thyroparathyroidectomized", "psychoneuroendocrinological"],
    9: ["otorhinolaryngological", "spectrophotofluorometrically", "hepaticocholangiocholecystenterostomies"],
    10: ["pneumonoultramicroscopicsilicovolcanoconiosis", "subdermatoglyphic", "uncharacteristically"]
}

# Function to start the game
def start_game():
    if st.session_state.level in word_levels:
        words_to_pronounce = word_levels[st.session_state.level]
        st.session_state.score += speech_therapy_game(words_to_pronounce)
        st.session_state.level += 1

# Display current score and level
st.write(f"Current Score: {st.session_state.score}")
st.write(f"Current Level: {st.session_state.level}")

# Show the next word to pronounce if the game has started
if 'current_word' in st.session_state:
    st.write(f"Pronounce the word: {st.session_state.current_word}")

# Button to start the game
if st.button("Start Game") or st.session_state.level in word_levels:
    start_game()

# Check if the user has completed all levels
if st.session_state.level > len(word_levels):
    st.write("Congratulations! You have completed all levels.")
    st.session_state.level = 1
    st.session_state.score = 0
