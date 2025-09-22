import msvcrt
import os

docSymbole = "🔷"
vide = "🔲"
dalekSymbole = "🔶"
feraille = "🔳"

vie = 1
docteurAncienX = 0
docteurAncienY = 0

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

dalek = Dalek(1,1,10,0,0)

grille = [
    [docSymbole, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, dalekSymbole, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, feraille, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, vide],
]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def deplacer_docteur(grille, nouveauX, nouveauY):
    global docteurAncienX
    global docteurAncienY
    grille[docteurAncienY][docteurAncienX] = vide
    grille[nouveauY][nouveauX] = docSymbole
    docteurAncienX = nouveauX
    docteurAncienY = nouveauY

def afficher_grille(grille):
    for ligne in grille:
        print("".join(ligne))

def on_key_event(keyPressed):
    if keyPressed == b'\xe0':
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
        print(f"Touche pressée : {key.decode()}")

def main():
    afficher_grille(grille)
    while True:
        keyPressed = msvcrt.getch()
        cls()
        on_key_event(keyPressed)
        deplacer_docteur(grille, doc.positionX, doc.positionY)
        afficher_grille(grille)

if __name__ == "__main__":
    main()

