import random

class generateurMDP:

    NOM_DICTIONNAIRE = "dictionnaire.txt"

    def __init__(self, nbVM):
        self.nbVM = nbVM
        self.listeFamille = []
        self.listeMot = self.lireMDP()
        self.tailleListe = len(self.listeMot)
        self.genererListIndex()


    def lireMDP(self):
        listeMot = []
        with open(generateurMDP.NOM_DICTIONNAIRE, 'r') as file:
            for line in file:
                listeMot.append(line.strip())
        return listeMot

        
    def genererNombre(tailleListe):
        return random.randint(0, tailleListe)

    def genererListIndex (self):
        listeIndex = []
        for i in range(5):
            random_number = self.genererNombre(self.tailleListe)
            for index in listeIndex:
                if index == random_number:
                    i-=1
                else :
                    listeIndex.append(random_number)
