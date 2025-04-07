import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()

placeholder_str = " ".join(["_" for _ in chosen_word])
print(placeholder_str)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ["_" for _ in chosen_word]
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = letter
    else:
        print(" ".join(display))

