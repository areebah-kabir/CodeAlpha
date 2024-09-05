import random

# Word list for the game
words = ["python", "java", "hangman", "programming", "developer"]

# Function to choose a random word from the list
def get_random_word():
    return random.choice(words)

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Main Hangman game function
def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_guesses:
        print(f"\nYou have {max_guesses - incorrect_guesses} guesses left.")
        print(display_word(word, guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word '{word}'. You win!")
                break
        else:
            incorrect_guesses += 1
            print(f"'{guess}' is not in the word.")
    
    if incorrect_guesses == max_guesses:
        print(f"Sorry, you've run out of guesses. The word was '{word}'. Better luck next time!")

# Run the Hangman game
if __name__ == "__main__":
    hangman()
