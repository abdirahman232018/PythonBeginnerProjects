#author: Abdirahman Abdi

import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
hangman_logo=hangman_art.logo
print(hangman_logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"The word is {len(display)} letters")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    correct_guesses=""
    if guess in correct_guesses:
        print(f"You already gussed {guess}, try another letter")
    if guess in chosen_word and guess not in correct_guesses:
        correct_guesses+=guess
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    wrong_guesses=""
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in wrong_guesses:
            print(f"The letter {guess} not in the word")
        if guess in wrong_guesses:
            print(f"The letter {guess} not in the word")
            print(f"You already chose {guess}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'Pssst, the solution was {chosen_word}.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])