import math
import random
from select import select
from tkinter import Y

class FormuleAffine:
    
    def __init__(self,coef_direc = 1,y = 0):
        self.coef_direc = coef_direc
        self.y = Y

    def calcul(self,x):
        return self.y+self.coef_direc*x