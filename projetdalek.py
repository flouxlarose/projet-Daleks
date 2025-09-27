import msvcrt
import os
from random  import randint     # retourne un entier aléatoire entre 2 numéros inclus

docSymbole = "🔷"
vide = "🔲"
dalekSymbole = "🔶"
feraille = "🔳"

nbVie = 1
nbBlaster = 3
docteurAncienX = 0
docteurAncienY = 0
nbDeplacement = 0
nbDalek = 0
score = 0
niveau = 0
meilleurParties = []

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
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def deplacer_docteur(grille, nouveauX, nouveauY):
    global docteurAncienX
    global docteurAncienY
    global nbDeplacement
    global niveau
    grille[docteurAncienY][docteurAncienX] = vide
    grille[nouveauY][nouveauX] = docSymbole
    docteurAncienX = nouveauX
    docteurAncienY = nouveauY
    nbDeplacement+=1
    if nbDeplacement % 3 == 0:
        creer_dalek(1, 1, 10)
        niveau += 1

def deplacer_dalek(dalek: Dalek):
    x, y = dalek.position
    direction = randint(0, 3)

    if direction == 0:  # UP
        if y > 0:
            grille[y][x] = vide
            dalek.position[1] -= 1
    elif direction == 1:  # RIGHT
        if x < 9 - 1:
            grille[y][x] = vide
            dalek.position[0] += 1
    elif direction == 2:  # DOWN
        if y < 8 - 1:
            grille[y][x] = vide
            dalek.position[1] += 1
    elif direction == 3:  # LEFT
        if x > 0:
            grille[y][x] = vide
            dalek.position[0] -= 1

    grille[dalek.position[1]][dalek.position[0]] = dalekSymbole
    dalek.positionX = dalek.position[0]
    dalek.positionY = dalek.position[1]

def creer_dalek(vie, deplacement, valeur):
    global nbDalek
    while True:
        randomX = randint(0, 8)  
        randomY = randint(0, 7) 
        if grille[randomY][randomX] == vide:
            x, y = randomX, randomY
            break

    dalek = Dalek(vie,deplacement,valeur,x,y)
    collectionDalek.append(dalek)
    grille[y][x] = dalekSymbole
    nbDalek+=1
    

def afficher_grille(grille):
    for ligne in grille:
        print("".join(ligne))

def on_key_event(keyPressed):
    if keyPressed == b'q':
        blaster()
    elif keyPressed == b'\x00':
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

def afficher_infos(nbBlaster, score, niveau):
    print(f"Score : {score}")
    print(f"Niveau : {niveau}")
    print(f"Blaster shot : {nbBlaster}")

def detruire_dalek(x, y):
    global score
    for i in range(len(collectionDalek) - 1, -1, -1):  
        dalek = collectionDalek[i]
        if dalek.position == [x, y]:
            grille[dalek.positionY][dalek.positionX] = vide
            score += 100
            del collectionDalek[i]

def blaster():
    global nbBlaster 
    if nbBlaster < 1:
        return False
    else:
        nbBlaster -= 1
        detruire_dalek(doc.positionX, doc.positionY + 1) # right
        detruire_dalek(doc.positionX, doc.positionY - 1) # left
        detruire_dalek(doc.positionX + 1, doc.positionY) # down
        detruire_dalek(doc.positionX - 1, doc.positionY) # up
        detruire_dalek(doc.positionX + 1, doc.positionY + 1) 
        detruire_dalek(doc.positionX - 1, doc.positionY - 1) 
        detruire_dalek(doc.positionX + 1, doc.positionY - 1) 
        detruire_dalek(doc.positionX - 1, doc.positionY + 1) 


def verifier_collision_docteur_dalek():
    for dalek in collectionDalek:
        if dalek.position == [doc.positionX, doc.positionY]:
            meilleurParties.append(score)
            print("\033[91mGAME OVER\033[0m")
            menu()

def classement():
    print("Classement des meilleures parties\n\n")
    for i, s in enumerate(sorted(meilleurParties), 1):
        print(f"{i}. {s}")
    print("\nq = Retour au menu")
    choix = msvcrt.getch()
    if choix == b'q':
        cls()
        menu()
    else:
        cls()
        classement()

def menu():
    print("Options\n")
    print("1. jouer")
    print("2. classement")
    choix = msvcrt.getch()
    if choix == b'1':
        cls()
        main_jeu()
    elif choix == b'2':
        cls()
        classement()
    else:
        cls()
        menu()

def main_jeu():
    creer_dalek(1,1,10)
    afficher_grille(grille)
    afficher_infos(nbBlaster, score, niveau)
    while True:
        keyPressed = msvcrt.getch()
        cls()
        on_key_event(keyPressed)
        deplacer_docteur(grille, doc.positionX, doc.positionY)
        verifier_collision_docteur_dalek()
        for dalek in collectionDalek:
            deplacer_dalek(dalek)
        verifier_collision_docteur_dalek()
        afficher_grille(grille)
        afficher_infos(nbBlaster, score, niveau)

if __name__ == "__main__":
    menu()
