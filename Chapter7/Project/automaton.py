"""
def welcome(name):
    print("Bienvenue " + name + "!")

name = str(input("Veuillez entrer votre nom: "))
welcome(name)
"""

def welcome():
    name = str(input("Merci de contacter Thibault! Je peux avoir votre prénom? "))
    print("Bienvenue chez Thibault, " + name + "!")
    return

def choose_category():
    print("*** Menu général Thibault ***\n"
          "[1] Horaires & Accès \n"
          "[2] Gestion de commande \n"
          "[3] Suivi de livraison \n"
          "[4] Suggestion de produit \n"
          "[5] Autre sujet")
    category = int(input("Choisissez une des catégories en tapant un chiffre entre 1 et 5: "))


welcome()
choose_category()