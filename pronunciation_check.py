def check_pronunciation(expected_word, user_word):
    return expected_word.lower() == user_word.lower()

# Test the pronunciation check functionality
if __name__ == "__main__":
    expected = "apple"
    user_pronunciation = "Apple"
    if check_pronunciation(expected, user_pronunciation):
        print("Correct pronunciation!")
    else:
        print("Try again.")
