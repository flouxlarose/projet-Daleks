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






