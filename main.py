import random
import hangman_words as hw
import hangman_art as ha

print(f"{ha.logo}\n")

chosen_word = random.choice(hw.word_list)

lives = 6

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Creating blanks
display = []
for letter in chosen_word:
    display.append("_")

end_game = False

while not end_game:
    guess = input("\nGuess a letter: ").lower()
  
    if guess in display:
      print(f"Hey, '{guess}' was one of your previous guesses already!")
    
    # Check guessed letter
    for index in range(0, len(chosen_word)):
        letter = chosen_word[index]   
        if letter == guess:
            display[index] = guess

    print(" ".join(display))

    # Check if user runs out of lives before finding all the right letters (LOSE)
    if guess not in chosen_word:
      lives -= 1
      print(f"\n'{guess}' was NOT one of the correct letters.\n[-1 life] => {lives} lives remaining!")
      if lives == 0:
        end_game = True
        print("\nYou fool! You've lost. :x")

    # Check if user found all the right letters (WIN)
    if "_" not in display:
        end_game = True
        print("\nCongratulations! You've won. ;D")

    # Print the ASCII art from 'stages' (the list) that corresponds to the current number of 'lives' the user has remaining
    print(ha.stages[lives])