import random
from random import seed
from random import choice

seed(1)
# seed random number generator

print("Dice Roller by TechMT")
dice = int(input(f"What dice would you like to roll?"))
#gets the type of dice
number_of_rolls = int(input("How many times?"))
#gets how many rolls you want


# make choices from the sequence
for _ in range(number_of_rolls):
    sequence = [i for i in range(dice)]
    # prepare a sequence
    selection = choice(sequence)
    #gets a random number in the dice
    print(selection + 1)
