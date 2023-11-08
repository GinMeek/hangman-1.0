# Hangman Game: A word guessing game where the player tries to complete a hidden word by guessing individual letters.

# Import necessary modules.
import random
import hangman_art as hma
import hangman_word as hmw

# Randomly select a word from the list of words.
chosen_word = random.choice(hmw.word_list)

# Create a display list to represent the current state of the word, initially filled with underscores.
display = ['_'] * len(chosen_word)

# Create a set to store guessed letters and initialize the player's remaining lives to 6.
guess_list = set()
life = 6

# Print the game's logo.
print(hma.logo)

# Main game loop.
while True:
    # Display the current state of the word with underscores.
    print('\n' + ' '.join(display) + '\n')

    # Get a letter guess from the player and ensure it is a single alphabetical character.
    guess = input('Guess a letter: ').lower()

    if not guess.isalpha() or len(guess) != 1:
        print('\nInvalid input. Please enter a single letter.\n')
        continue

    # Check if the guessed letter has already been guessed.
    if guess in display or guess in guess_list:
        print(
            f"\nYou've already guessed the letter {guess}. Try another letter.")
        print("You've guessed the following letters: " + ' '.join(guess_list))
        continue

    # Add the guessed letter to the set of guessed letters.
    guess_list.add(guess)

    # Check if the guessed letter is in the chosen word.
    if guess in chosen_word:
        for position, letter in enumerate(chosen_word):
            if guess == letter:
                display[position] = letter
    else:
        # If the guessed letter is not in the word, decrement the player's remaining lives.
        life -= 1
        print(f'\nYou guessed the letter {guess}, which is not in the word.')
        print(f'You lose a life. Current hangman stage: {hma.stages[life]}\n')

    # Check if the word has been fully guessed by the player.
    if '_' not in display:
        print('\n\nYou win!')
        break

    # Check if the player has run out of lives.
    if life == 0:
        print('\n\nYou lose!')
        break
