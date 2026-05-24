import random

# List of predefined words
words = ["apple", "tiger", "house", "robot", "music"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_guesses:

    # Display word progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check guess
    if guess in word:
        print("Correct Guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong Guess!")
        wrong_guesses += 1
        print(f"Remaining chances: {max_guesses - wrong_guesses}")

# Game over
if wrong_guesses == max_guesses:
    print("Game Over!")
    print("The word was:", word)