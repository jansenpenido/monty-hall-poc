"""
Monty Hall POC
--------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

import sys,random

print("Welcome to Monty Hall!")

random.seed()

won = 0
lost = 0
choice = 0
games = 100000

print("Would you like to swap doors?")
print("[Y]es or [N]o: "),
c = input()

if c.upper() == 'Y':
    swap = True
else:
    swap = False

doors = ["goat", "goat", "car"]

for i in range(games):

    random.shuffle(doors)

    choice = random.randrange(3)

    for i, val in enumerate(doors):
        if doors[i] == "goat" and i != choice:
            presenter = i
            break

    if swap == True:
        choice = random.randrange(3)

        while( choice == presenter ):
            choice = random.randrange(3)

    if doors[choice] == "car":
        won += 1
    else:
        lost += 1

print("Time is up! Here are the results:")

win_percent = "{0:.2f}%".format(float(won) / float(games) * 100)
lost_percent = "{0:.2f}%".format(float(lost) / float(games) * 100)


print("Wins: " + win_percent + " (" + str(won) + " times)")
print("Losses: " + lost_percent + " (" + str(lost) + " times)")
