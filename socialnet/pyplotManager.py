import matplotlib.pyplot as plt
from Utilisateur import Utilisateur
from Page import Page

class PyplotManager:



    def __init__(self, g):
        self.deja = False

    def prepa(self, g): #prepare l'affichage du graph
        tous = []
        sommets_fic = {}
        i = 0
        for sommet in g.get_sommets():
            if isinstance(sommet, Page):
                tous.append([i, 10, "P", sommet])
                self.addPoint([i, 10], "P")
            elif isinstance(sommet, Utilisateur):
                tous.append([i, 5, "U", sommet])
                self.addPoint([i, 5], "U")
            sommets_fic[i] = sommet
            i = i + 1
        for idf in sommets_fic.keys():
            sommet = sommets_fic.get(idf)
            for id2 in sommets_fic.keys():
                sommet2 = sommets_fic.get(id2)
                if sommet2 in sommet.get_connections():
                    self.drawArrow(tous[idf], tous[id2])
        for idf in sommets_fic.keys():
            sommet = sommets_fic.get(idf)
            if isinstance(sommet, Page):
                if sommet.get_admins() != None:
                    admins = sommet.get_admins()
                    for possible in sommets_fic:
                        if sommets_fic.get(possible) in admins:
                            self.drawArrow(tous[idf], tous[possible])

    def refresh(self, g): #refresh l'affichage du graph
        self.close()
        self.prepa(g)
        self.affiche(g)

    def drawArrow(self, A, B): #ajoute un fleche
        plt.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1], head_width=0.05, head_length=0.1, fc='k', ec='k', length_includes_head=True)

    def addPoint(self, A, type): #ajoute un point
        if type == "P":
            plt.scatter(A[0], A[1], marker='p', s=80)
        elif type == "U":
            plt.scatter(A[0], A[1], marker='x', s=80)

    def close(self):
        plt.close()

    def affiche(self, g):
        self.deja = True
        plt.show(block=False)

    def getdeja(self):
        return self.deja
