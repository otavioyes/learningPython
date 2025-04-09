import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
game_over = False
correct_letter = []

display = ""

#enquanto não for game over
while not game_over:
    #imprima
    guess = input("Guess a letter: ").lower()

#para cada letra em chosen_word
    for letter in chosen_word:
    
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter == guess:
            display += letter
        else:
            display = "_"

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    print(display)

if "_" not in display:
    game_over = True
    print("You win.")

