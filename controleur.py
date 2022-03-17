from datetime import datetime, timedelta
import os
class Controleur:
    def __init__(self,taille = 10,periode = 1):
        self.listeFormule = []
        self.periode = periode
        self.taille = taille
    
    def addFormule(self,formule):
        self.listeFormule.append(formule)

    def calcul(self,nom_fichier):
        
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
            
        f = open(nom_fichier, "a")
        
        date = datetime.now()
        
        entete = "date,"
        for index in range(len(self.listeFormule)):
                entete += str(index)+","
        entete = entete[:-1]+"\n"; 
        f.write(entete) 
        
        for x in range(self.taille):
            texte = str(date.strftime("%H:%M:%S %Y/%m/%d"))+","   
            
            for formule in self.listeFormule:
                texte += str(str(formule.calcul(x/self.periode)) +",")
            texte = texte[:-1]+"\n";
            f.write(texte) 
            
            date +=  timedelta(seconds=self.periode)
        f.close()