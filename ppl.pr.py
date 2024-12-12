import random
# for ● ┌ ─ ┐ │ └ ┘ = print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# "┌────────┐",
# "│        │",
# "│        │",
# "│        │",
# "└────────┘"
# Define the graphical representations of dice faces
face={

    1:("┌───────┐",
       "│       │",
       "│   ●   │",
       "│       │",
       "└───────┘"),
    2:("┌───────┐",
       "│       │",
       "│●     ●│",
       "│       │",
       "└───────┘"),
    3:("┌───────┐",
       "│   ●   │",
       "│       │",
       "│●     ●│",
       "└───────┘"),
    4:("┌───────┐",
       "│●     ●│",
       "│       │",
       "│●     ●│",
       "└───────┘"),
    5:("┌───────┐",
       "│●     ●│",
       "│   ●   │",
       "│●     ●│",
       "└───────┘"),
    6:("┌───────┐",
       "│●     ●│",
       "│●     ●│",
       "│●     ●│",
       "└───────┘")
}
# Get user input for number of dice and number of sides

dice = int(input("Number of dice:"))
sides= int(input("Number of sides: "))

import time
for i in range(101):
    print(f'\rrolling...{i}',end="")
    time.sleep(0.04)
print()

# Validation checks
if dice<1 :
    print("ERROR! , Atleast one dice must")
    quit()
if sides < 2 or sides > 6:
    print("ERROR! , Atleast 2 and atmost 6 sides must ")
    quit()
    
# Roll the dice
roll=[]

for i in range(dice):
    num1=random.randint(1,sides)
    roll.append(num1)


# Print the rolled dice faces

for i in roll:
    for die in face[i]:
        print(die)

# Print the roll results
print("Roll result=", roll)