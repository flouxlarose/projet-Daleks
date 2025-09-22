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

class Dalek:
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

collectionDalek = []
dalek1 = Dalek(2,3,4,5,6)
dalek1.position = 2
dalek2 = Dalek(2,3,4,5,6)
dalek3 = Dalek(2,3,4,5,6)
collectionDalek.append(dalek1)
collectionDalek.append(dalek2)
collectionDalek.append(dalek3)
collectionDalek[1]



def mooveEntity(x, y, deplacement):
    direction = ["up", "right", "down", "left"]
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