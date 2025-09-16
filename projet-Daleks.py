class Docteur:
    def __init__(self, vie, deplacement, x, y):
        self.vieDocteur = vie
        self.zappeur = True
        self.teleporteur = True
        self.deplacementDocteur = deplacement
        self.creditCosmique = 0
        self.position = [x, y]

    class dalek:
        def __init__(self, vie, deplacement, valeur, x, y):
            self.vieDalek = vie
            self.deplacementDalek = deplacement
            self.valeurCosmique = valeur
            self.position = [x, y]



