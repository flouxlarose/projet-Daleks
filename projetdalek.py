import msvcrt
import os
from random  import randint     # retourne un entier aléatoire entre 2 numéros inclus

docSymbole = "🔷"
vide = "🔲"
dalekSymbole = "🔶"
feraille = "🔳"

nbVie = 1
nbBlaster = 1
docteurAncienX = 0
docteurAncienY = 0
nbDeplacement = 0
nbDalek = 0

class Docteur:
    def __init__(self, vie, deplacement, x, y):
        self.vieDocteur = vie
        self.zappeur = True
        self.teleporteur = True
        self.deplacementDocteur = deplacement
        self.creditCosmique = 0
        self.positionX = x
        self.positionY = y

doc = Docteur(1,1,0,0)

class Dalek:
    def __init__(self, vie, deplacement, valeur, x, y):
        self.vieDalek = vie
        self.deplacementDalek = deplacement
        self.valeurCosmique = valeur
        self.positionX = x
        self.positionY = y
        self.position = [x,y]

collectionDalek:list[Dalek] = []

grille = [
    [docSymbole, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, feraille, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def deplacer_docteur(grille, nouveauX, nouveauY):
    global docteurAncienX
    global docteurAncienY
    global nbDeplacement
    grille[docteurAncienY][docteurAncienX] = vide
    grille[nouveauY][nouveauX] = docSymbole
    docteurAncienX = nouveauX
    docteurAncienY = nouveauY
    nbDeplacement+=1
    if nbDeplacement % 3 == 0:
        creer_dalek(1, 1, 10, 0, 0)

def deplacer_dalek(dalek: Dalek):
    direction = randint(0, 3)

    if direction == 0 and grille[(dalek.position[1] - 1) % 8][dalek.position[0]] == vide:     # direction UP
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[1] = (dalek.position[1] - 1) % 8      
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole

    elif direction == 1 and grille[dalek.position[1]][(dalek.position[0] + 1) % 9] == vide:   # direction RIGHT
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[0] = dalek.position[0] + 1 % 9
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole

    elif direction == 2 and grille[(dalek.position[1] + 1) % 8][dalek.position[0]] == vide:   # direction DOWN        
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[1] = dalek.position[1] + 1 % 8
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole

    elif direction == 3 and grille[dalek.position[1]][(dalek.position[0] - 1) % 9] == vide:   # direction LEFT
        grille[dalek.position[1]][dalek.position[0]] = vide
        dalek.position[0] = dalek.position[0] - 1 % 9
        grille[dalek.position[1]][dalek.position[0]] = dalekSymbole


def creer_dalek(vie, deplacement, valeur, x, y):
    global nbDalek
    dalek = Dalek(vie,deplacement,valeur,x,y)
    collectionDalek.append(dalek)
    grille[y][x] = dalekSymbole
    nbDalek+=1


def afficher_grille(grille):
    for ligne in grille:
        print("".join(ligne))

def on_key_event(keyPressed):
    if keyPressed == b'q':
        blaster(nbBlaster)
    elif keyPressed == b'\xe0':
        key2 = msvcrt.getch()
        if key2 == b'H':
            if doc.positionY > 0:
                doc.positionY -= 1              
        elif key2 == b'P':
            if doc.positionY < 7:
                doc.positionY += 1
        elif key2 == b'K':
            if doc.positionX > 0:
                doc.positionX -= 1
        elif key2 == b'M':
            if doc.positionX < 8:
                doc.positionX += 1
    else:
        return False

def afficher_infos(vie, nbBlaster, nbDalek):
    print(f"nombre de vie : {vie}" )
    print(f"blaster shot : {nbBlaster}")
    print(f"nombre de dalek : {nbDalek}")

def detruire_dalek(x, y):
    for i in range(len(collectionDalek) - 1, -1, -1):  
        dalek = collectionDalek[i]
        if dalek.position == [x, y]:
            grille[dalek.positionY][dalek.positionX] = vide
            del collectionDalek[i]

def blaster(nbBlaster):
    if nbBlaster < 1:
        return False
    else:
        detruire_dalek(doc.positionX, doc.positionY + 1)
        detruire_dalek(doc.positionX, doc.positionY - 1)
        detruire_dalek(doc.positionX + 1, doc.positionY)
        detruire_dalek(doc.positionX - 1, doc.positionY)



def main():
    creer_dalek(1,1,10,1,1)
    afficher_grille(grille)
    afficher_infos(nbVie, nbBlaster, nbDalek)
    while True:
        keyPressed = msvcrt.getch()
        cls()
        on_key_event(keyPressed)
        deplacer_docteur(grille, doc.positionX, doc.positionY)
        for dalek in collectionDalek:
            deplacer_dalek(dalek)
        afficher_grille(grille)
        afficher_infos(nbVie, nbBlaster, nbDalek)


if __name__ == "__main__":
    main()

