import random
import hangman_words
import stages
import logo

print(logo.logo)
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"



while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in display:
        print(f"You have already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      print(f"You guessed '{guess}' wrong, You lose a LIFE!")
      lives -= 1

      if lives == 0:
        end_of_game = True
        print(f"You Lose The word is {chosen_word}")
        

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(stages.stages[lives])