import keyboard
import msvcrt
# Grille

COL = 4
LIG = 10
vie = 1

docSymbole = "D"
vide = "#"
dalekSymbole = "X"
feraille = "o"


docteurAncienX = 0
docteurAncienY = 0

grille = [
    [docSymbole, vide, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, dalekSymbole, vide, vide],
    [vide, dalekSymbole, vide, vide, vide, vide, vide, vide, vide, vide],
    [vide, vide, vide, vide, vide, vide, vide, vide, dalekSymbole, vide],
]

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

def deplacer_docteur(grille, ancienX, ancienY, nouveauX, nouveauY):
    grille[ancienY][ancienX] = vide
    grille[nouveauY][nouveauX] = doc

def afficher_grille(grille):
    for ligne in grille:
        print("".join(ligne))

def on_key_event(keyPressed):
    if keyPressed == b'\xe0':
        key2 = msvcrt.getch()
        if key2 == b'H':
            doc.positionY -= 1
        elif key2 == b'P':
            doc.positionY += 1
        elif key2 == b'K':
            doc.positionX -= 1
        elif key2 == b'M':
            doc.positionY += 1
    else:
        print(f"Touche pressée : {key.decode()}")

def main():
    afficher_grille(grille)
    while True:
        keyPressed = msvcrt.getch()
        on_key_event(keyPressed)
        deplacer_docteur(grille, docteurAncienX, docteurAncienY, doc.positionX, doc.positionY)
        afficher_grille(grille)

if __name__ == "__main__":
    main()

