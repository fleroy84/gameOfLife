# -*- coding: utf-8 -*-
from time import clock
import csv

class chronometre():
    def __init__(self):
        self.raz()
        self.initfile()
    
    def chronostart(self):
        self.temps_initial = clock()
    
    def chronostop(self):
        self.temps_courant = clock()
        self.duree_cumulee += self.duree()
        self.temps_initial = clock()
    
    def initfile(self):
        with open("chrono.csv", "w", newline = "", encoding = "utf8") as f:
            ecrire = csv.writer(f)
            ligne = ["Génération", "NbreCellules", "Temps"]
            ecrire.writerow(ligne)
    
    def tofile(self, gen, nb):
        with open("chrono.csv", "a", newline = "", encoding = "utf8") as f:
            ecrire = csv.writer(f)
            ligne = [str(gen), str(nb), str(self.duree_cumulee)]
            ecrire.writerow(ligne)
            
    def duree(self):
        return self.temps_courant - self.temps_initial
    
    def raz(self):
        self.temps_initial = 0.0
        self.temps_courant = 0.0
        self.duree_cumulee = 0.0
