from random  import randint     # retourne un entier aléatoire entre 2 numéros inclus


#  Définition des deux classes principal et nécéssaire
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
        self.positionX = x
        self.positionY = y
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

def creerDalek(vie, deplacement, valeur, x, y):
    dalek = Dalek(vie,1,5,5,5)
    collectionDalek.append(dalek)
    grille[y][x] = dalekSymbole


# liste de tout les dalek
collectionDalek:list[Dalek] = []
# comment creer un nouveau dalek
dalek = Dalek(2,3,4,5,6)
# rajouter le dalek a la liste
collectionDalek.append(dalek)

print(collectionDalek[0].valeurCosmique)

def detruire_Dalek(x1,y1, ):
    global Dalek
    detruire = False
    compteurBoucle = 0
    for Dalek in collectionDalek:
        if collectionDalek[compteurBoucle].position[0] == x and collectionDalek[compteurBoucle].position[1] == y:
            detruire = True
            id = compteurBoucle
        compteurBoucle += 1
    if detruire:
       del collectionDalek[id]


def deplacer_docteur(grille, nouveauX, nouveauY):
    global docteurAncienX
    global docteurAncienY
    grille[docteurAncienY][docteurAncienX] = vide
    grille[nouveauY][nouveauX] = docSymbole
    docteurAncienX = nouveauX
    docteurAncienY = nouveauY

#  PREND UN NOMBRE RANDOM ENTRE 0 ET 3 (0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT)
def deplacer_dalek(dalek: Dalek, direction):
    if direction == 0 and grille[dalek.position[0]][dalek.position[0]] == vide:
        x -= 1        
    elif direction[random] == "right":
        x += deplacement 
    elif direction[random] == "down":
        y += deplacement
    elif direction[random] == "left":
        x -= deplacement

def mooveEntity(x, y, deplacement):
    direction = ["up", "right", "down", "left"]
    random = randint(0, 3)
    
    if grille[y[x]] == vide :
        print("cum")


creerDalek(1,1,1,0,0)
detruire_Dalek(0,0)

