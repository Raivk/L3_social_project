import matplotlib.pyplot as plt
from Utilisateur import Utilisateur
from Page import Page
import random

class PyplotManager:



    def __init__(self, g):
        self.deja = False
        self.tous = []

    def prepa(self, g): #prepare l'affichage du graph
        sommets_fic = {}
        i = 0

        for sommet in g.get_sommets():
            valid = False
            for elem in self.tous:
                if elem[3] == sommet:
                    self.addPoint(self.tous[i])
                    valid = True
            if valid == False:
                randx, randy = self.randvalid()
                if isinstance(sommet, Page):
                    self.tous.append([randx, randy, "P", sommet])
                    self.addPoint(self.tous[i])
                elif isinstance(sommet, Utilisateur):
                    self.tous.append([randx, randy, "U", sommet])
                    self.addPoint(self.tous[i])
                sommets_fic[i] = sommet
            i = i + 1
        for idf in sommets_fic.keys():
            sommet = sommets_fic.get(idf)
            for id2 in sommets_fic.keys():
                sommet2 = sommets_fic.get(id2)
                if sommet2 in sommet.get_connections():
                    self.drawArrow(self.tous[idf], self.tous[id2])
        for idf in sommets_fic.keys():
            sommet = sommets_fic.get(idf)
            if isinstance(sommet, Page):
                if sommet.get_admins() != None:
                    admins = sommet.get_admins()
                    for possible in sommets_fic:
                        if sommets_fic.get(possible) in admins:
                            self.drawArrow(self.tous[idf], self.tous[possible])


    def randvalid(self):
        valid = False
        while not valid:
            randx = random.randint(0, 10)
            randy = random.randint(0, 10)
            if self.tous == []:
                valid = True
            for elem in self.tous:
                if elem[0] != randx and elem[1] != randy:
                    valid = True
        return randx, randy

    def refresh(self, g): #refresh l'affichage du graph
        self.close()
        self.prepa(g)
        self.affiche(g)

    def drawArrow(self, A, B): #ajoute un fleche
        plt.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1], head_width=0.05, head_length=0.1, fc='k', ec='k', length_includes_head=True)

    def addPoint(self,sommet): #ajoute un point
        if sommet[2] == "P":
            plt.scatter(sommet[0], sommet[1], marker='p', s=80)
            plt.annotate(sommet[3].get_nom(),(sommet[0],sommet[1]))
        elif sommet[2] == "U":
            plt.scatter(sommet[0], sommet[1], marker='x', s=80)
            plt.annotate(sommet[3].get_nom(), (sommet[0], sommet[1]))

    def close(self):
        plt.close()

    def affiche(self, g):
        self.deja = True
        plt.show(block=False)

    def getdeja(self):
        return self.deja
