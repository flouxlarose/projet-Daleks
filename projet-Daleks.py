from random  import randint     # retourne un entier aléatoire entre 2 numéros inclus

class Docteur:
    def __init__(self, vie, deplacement, x, y):
        self.vieDocteur = vie
        self.zappeur = True
        self.teleporteur = True
        self.deplacementDocteur = deplacement
        self.creditCosmique = 0
        self.positionX = x
        self.positionY = y

class dalek:
    def __init__(self, vie, deplacement, valeur, x, y):
        self.vieDalek = vie
        self.deplacementDalek = deplacement
        self.valeurCosmique = valeur
        self.position = [x, y]

docSymbole = "D"
vide = "#"
dalekSymbole = "X"
feraille = "o"

def afficher_grille(grille):
    for ligne in grille:
        print("".join(ligne))

grille = [
    [docSymbole, vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, dalekSymbole, vide, vide],
    [vide, dalekSymbole, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, dalekSymbole, vide],
]

afficher_grille(grille)

direction = ["up", "right", "down", "left"]

def mooveEntity(x, y, deplacement):
    random = randint(0, 3)
    if direction[random] == "up":
        y -= 1
    elif direction[random] == "right":
        x += 1 
    elif direction[random] == "down":
        y += 1
    elif direction[random] == "left":
        x -= 1
    if grille[y[x]] == vide :
        print("cum")