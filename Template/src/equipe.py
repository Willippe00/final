class equipe:
    def __init__(self, couleur,nbPlayer,symbole,nom):
        self.couleur = couleur
        self.nbPlayer = nbPlayer
        self.symbole = symbole
        self.nom = nom
        self.listePlayer = []

    def getNomEquipe(self):
        return self.nom
    
    def getNbPlayer(self):
        return self.nbPlayer
    
    def getPlayer (self, index):
        return self.listePlayer[index]
    
    def setPlayer (self, listePlayer):
        self.listePlayer = listePlayer

    def addPlayer (self,newPlayer):
        self.listePlayer.append(newPlayer)
    def getSize(self):
        return len(self.listePlayer)

    def getEquipe(self):
        return self.listePlayer
    
class equipeAttaque(equipe):
    equipeVictime = ""

class equipeVictime(equipe):
    equipeAttaque = ""