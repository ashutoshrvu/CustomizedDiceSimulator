# Customized Dice Simulator

# Importing random library
import random

# Defining a function to customize the dice throw
def dice_throw():
    customization = [1, 2, 5, 3, 6]
    print(random.choice(customization))

# Script for the user
print("""Press 1 to roll the dice
Press 2 to exit the game
- """)
key = int(input())

if key == 1:
    dice_throw()
else:
    print("Goodbye!")