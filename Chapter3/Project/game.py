import random
"""
player = int(input("Que voulez-vous jouer? Pierre(1) / Ciseaux(2) / Papier(3). "))
computer = 1
if player == 2:
    print("L'ordinateur gagne.")
elif player == 3:
    print("Le player gagne.")
elif player == 1:
    print("Les deux côtés sont à égalité.")
"""

player = int(input("Que voulez-vous jouer? Pierre(1) / Ciseaux(2) / Papier(3). "))
computer = random.randint(1, 3)
if (player == 3 and computer == 1) or (player == 2 and computer == 3) or (player == 1 and computer == 2):
    print("Le player gagne. ")
elif player == computer:
    print("Les deux côté sont à égalité. ")
else:
    print("L'ordinateur gagne.")
