print(r'''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You are at a crossroads, deciding which way to go "left" or "right":  ')

if choice1 == "left":
    choice2 = input('You are a lost in the forest, do you "make a fire" '
                    'or "keep walking"?: ')

    if choice2 == "make a fire":
        choice3 = input('Good choice, it is morning and the beasts have gone to rest,'
        'do you "build a hut" or look for a "river"?: ')

        if choice3 == "river":
            choice4 = input('You re almost there! You ve found a cave with bats and a\n '
                            'waterfall with crystal clear water. Do you believe the treasure is\n '
                            'in the "cave" or inside the "waterfall"?: ')
            if choice4 == "cave":
                print("YOU WON! CONGRATULATIONS!")
            else:
                print("You slipped when crossing the waterfall! GAME OVER!")

    else: print("You kept walking and were attacked by a poisonous snake "
                "and died of asphyxiation! GAME OVER!")
else:
    print("You fell into a quicksand pit and were swallowed! GAME OVER!")

