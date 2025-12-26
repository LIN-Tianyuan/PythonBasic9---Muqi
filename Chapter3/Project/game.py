import random

player = int(input("Que voulez-vous jouer? Pierre(1) / Ciseaux(2) / Papier(3). "))
computer = 1
if player == 2:
    print("L'ordinateur gagne.")
elif player == 3:
    print("Le joueur gagne.")
elif player == 1:
    print("Les deux côtés sont à égalité.")

