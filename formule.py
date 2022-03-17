import math
import random

class Formule:
    
    def __init__(self,nom = "",periode = 1,amplitude = 1, bruit = 0):
        self.nom = nom
        self.periode = periode
        self.amplitude = amplitude
        self.bruit = bruit
        self.listeFormule = []

    def calcul(self,x):
        bruit= self.bruit*(random.random()-0.5)
        y = math.sin(math.pi*2*(x/self.periode))*self.amplitude
        for formule in self.listeFormule:
            y += formule.calcul(x)
        return y + bruit
    
    def setPeriode(self,periode):
        if(periode <= 0):
            raise ValueError('La periode doit être superieur a 0')
        self.periode = periode

    def addFormule(self,formule):
        self.listeFormule.append(formule)
