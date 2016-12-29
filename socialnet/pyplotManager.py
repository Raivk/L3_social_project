import matplotlib.pyplot as plt
from Utilisateur import Utilisateur
from Page import Page

class PyplotManager:

    fig = plt.figure()
    ax = fig.add_subplot(111)

    def __init__(self, g):
        plt.ion()
        self.fig = plt.figure()
        self.prepa(g)


    def prepa(self, g): #preparation de l'affichage de graph
        self.ax = self.fig.add_subplot(111)
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



    def drawArrow(self, A, B): #ajoute un fleche
        self.ax.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1], head_width=0.05, head_length=0.1, fc='k', ec='k', length_includes_head=True)

    def addPoint(self, A, type): #ajoute un point
        if type == "P":
            self.ax.scatter(A[0], A[1], marker='p', s=80)
        elif type == "U":
            self.ax.scatter(A[0], A[1], marker='x', s=80)

    def refresh(self, g): #rafraichi entierrement le graph
        self.ax.clear()
        self.fig.clear()
        self.prepa(g)


    def affiche(self, g):# test de modification
        zert = 0
        while True:
            print(zert)
            if (zert == 10):
                self.drawArrow([0, 8], [1, 15])
                self.ax.scatter(1, 2, marker='p', s=80)
            elif (zert ==20):
                self.refresh(g)
            self.fig.canvas.draw()
            zert = zert + 1




