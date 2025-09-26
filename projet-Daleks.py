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
        self.position = [x,y]

docSymbole = "D"
vide = "#"
dalekSymbole = "X"
feraille = "o"

def afficher_grille(grille):
    for ligne in grille:
        print("".join(ligne))

grille = [
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
]


collectionDalek = []
def creerDalek(vie, deplacement, valeur, x, y):
    dalek = Dalek(vie,deplacement,valeur,x,y)
    collectionDalek.append(dalek)
    grille[y][x] = dalekSymbole


# liste de tout les dalek
# collectionDalek:list[Dalek] = []
# comment creer un nouveau dalek
# rajouter le dalek a la liste
# collectionDalek.append(dalek)

# print(collectionDalek[0].valeurCosmique)

def detruire_Dalek(x1,y1):
    global Dalek
    detruire = False
    compteurBoucle = 0
    for Dalek in collectionDalek:
        if collectionDalek[compteurBoucle].position[0] == x1 and collectionDalek[compteurBoucle].position[1] == y1:
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
# random = randint(0, 3)
def deplacer_dalek(dalek: Dalek):
    direction = randint(0, 3)

    if direction == 0 and grille[(dalek.position[1] - 1) % 4][dalek.position[0]] == vide:     # direction UP
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[1] = dalek.position[1] - 1 % 8        
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole

    elif direction == 1 and grille[dalek.position[1]][(dalek.position[0] + 1) % 10] == vide:   # direction RIGHT
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[0] = dalek.position[0] + 1 % 9
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole

    elif direction == 2 and grille[(dalek.position[1] + 1) % 4][dalek.position[0]] == vide:   # direction DOWN        
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[1] = dalek.position[1] + 1 % 8
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole

    elif direction == 3 and grille[dalek.position[1]][(dalek.position[0] - 1) % 10] == vide:   # direction LEFT
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[0] = dalek.position[0] - 1 % 9
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole


# TEST FONCTION POUR BOUGER LES DALEKS
# creerDalek(1, 1, 20, 4, 4)
# afficher_grille(grille)
# deplacer_dalek(collectionDalek[0])
# print("\n\n\n")
# afficher_grille(grille)

# print("what da helli")



def teleporteur(doc: Docteur):
    teleportValide = False
    while(not teleportValide):
        x = randint(0, 9)
        y = randint(0, 8)
        if(grille[y][x] == vide):
            teleportValide = True
            deplacer_docteur(grille, x, y)
        
