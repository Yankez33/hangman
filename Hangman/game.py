import random
from hangman_words import word_list
from hangman_art import *


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
lettersUsed = []

print(logo)
print("\nYou have 6 lives. Each missed guess costs one life. Guessing a letter you have already guessed costs one life. Choose your letters carefully!\n")
name = (input("What is your name?: "))
print(f"\nGood luck, {name}\n")


display = []
for _ in range(word_length):
    display += '_'

clue = len(chosen_word)
print(f"The word is {clue} letters long\n")


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if lives > 0:
        lettersUsed.append(guess)
        print(f"Letters Guessed: {lettersUsed}\n")
        # print(lettersUsed)
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!\n")
        lives -= 1
        print(f"You have {lives} lives left. ")
        if lives == 0:
            end_of_game = True
            print("You have no more lives left")
            print(loser, reaper)
            print(f"The chosen word was {chosen_word.upper()}")

    print(display)

    print(stages[lives])

    if '_' not in display:
        end_of_game = True
        print(winner, trophy)
       
