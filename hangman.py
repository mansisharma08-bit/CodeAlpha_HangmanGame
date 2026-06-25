import random

words_list = ["python", "code", "alpha", "game", "player"]
secret_word = random.choice(words_list)

display_word = ["_"] * len(secret_word)
attempts_left = 6
guessed_letters = []

print("--- Welcome to the Hangman Game! ---")
print("Total incorrect attempts allowed: 6")

while attempts_left > 0 and "_" in display_word:
    print("\nWord to guess: " + " ".join(display_word))
    print(f"Attempts left: {attempts_left}")
    print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    
    guess = input("Guess a letter: ").lower().strip()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
        
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue
        
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts_left -= 1

print("\n--- Game Result ---")
if "_" not in display_word:
    print(f"Congratulations! You won! The word was: {secret_word}")
else:
    print(f"Game Over! You ran out of attempts. The word was: {secret_word}")