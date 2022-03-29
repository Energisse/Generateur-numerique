import math
import random
from select import select

class FormuleMonoPeriode:
    
    def __init__(self,periode = 1,amplitude = 1, bruit = 0):
        self.periode = periode
        self.amplitude = amplitude
        self.bruit = bruit

    def calcul(self,x):
        bruit= self.bruit*(random.random()-0.5)
        if(self.periode == 0):
            y = self.amplitude
        else:
            y = math.sin(math.pi*2*(x/self.periode))*self.amplitude
        return y + bruit