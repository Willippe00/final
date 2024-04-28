class player:

   def __init__(self, ligne,equipe):
      self.numeroVM = ligne[0]
      self.nomVM = ligne[1]
      self.user = ligne[2]
      self.password = ligne[3]
      self.port = ligne[4]
      self.typeEquipe = ""
      self.equipe = equipe

        
   def getNomVM (self):
       return self.nomVM
   
   def getPort (self):
       return self.port

   def extraireProfil(self):
       return [self.numeroVM,self.nomVM,self.user,self.user,self.password, self.port]
   
   def afficher(self):
       chaine = (
            f"   ---- {self.equipe.getNomEquipe()} ----\n"
            f"   HOTE: {self.nomVM}\n"
            f"   UTILISATEUR: {self.user}\n"
            f"   MOT DE PASSE: {self.password}\n"
            f"   PORT: {self.port}\n"
        )
       return chaine

   
       

class playerAttaque(player):
    def __init__(self, profil,equipe,joueurCible):
          super().__init__(profil,equipe)
        #   self.equipe = equipe
          self.joueurCible = joueurCible
          self.typeEquipe = "ATTAQUE"
          
    def afficher(self):
        chaine = super().afficher()
        chaineAttaque =(
            f"{chaine}\n"
            f"   Votre equipe va attaquer:\n"
            f"   UTILISATEUR: {self.joueurCible.getUserCible()}\n"
            f"   PORT: {self.joueurCible.getPort()}\n"
            
        )
      #   chaineAttaque = "Votre equipe va attaquer: " , self.userCible
        return chaineAttaque
        
    
class playerVictime(player):
      def __init__(self, profil,equipe,userCible):
          super().__init__(profil,equipe)
        #   self.equipe = equipe
          self.userCible = userCible
          self.typeEquipe = "VICTIME"
          self.listeMDP = []

          
      def ajouterListeMDP(self,listeMDP):
          self.listeMDP = listeMDP


      def afficher(self):
        chaine = super().afficher()
        chaineVictime =(
            f"{chaine}\n"
            f"   La victime est :\n"
            f"   UTILISATEUR: {self.userCible}\n"
            f"   Choisir un des cinq mots de passe: {self.listeMDP}\n"
            
        )

        return chaineVictime
      
      def getUserCible(self):
          return self.userCible