import random

total = 0
computer = random.randint(1, 100)
guess = int(input("Veuillez entrer un nombre: "))
total = total + 1
while not computer == guess and not total == 5:
    if computer < guess:
        guess = int(input("Veuillez entrer un autre nombre plus petit : "))
        total = total + 1
    else:
        guess = int(input("Veuillez entrer un autre nombre plus grand : "))
        total = total + 1

if guess == computer and total <= 5:
    print("Vous avez bien deviné ! (%d essais au total )." % total)
else:
    print("Game over! Vous avez échoué !!!")