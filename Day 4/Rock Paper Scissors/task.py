import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the game ROCK, PAPER AND SCISSORS!\n")
options = [rock, paper, scissors]


user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f"YOU: {options[user]}")


choice_pc = random.randint(0, 2)
print(f"Computer chose: {options[choice_pc]}")

if user >= 3 or user < 0:
    print("Number invalid, please! enter a number valid!")
elif user == 0 and choice_pc == 0:
    print("Is'a draw!")
elif user == 0 and choice_pc == 1:
    print("COMPUTER WON")
elif user == 0 and choice_pc == 2:
    print("YOU WON")
elif user == 1 and choice_pc == 1:
    print("Is'a draw !")
elif user == 1 and choice_pc == 2:
   print("COMPUTER WON!")
elif user == 1 and choice_pc == 0:
    print("YOU WON!")
elif user == 2 and choice_pc == 0:
    print("COMPUTER WON")
elif user == 2 and choice_pc == 1:
    print("YOU WON")
else: print("Is'a draw !")





