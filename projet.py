
import Formule
import Controleur


controleur = Controleur(1000,30)
formule1 = Formule(20,1,0)
formule2 = Formule(20,1,1)
controleur.addFormule(formule1)
controleur.addFormule(formule2)
controleur.calculate()