from Utilisateur import Utilisateur
from Page import Page
from Sommet import Sommet


class Graphe:

    def __init__(self):
        self.sommets = []

    def get_sommets(self):
        return self.sommets

    def add_sommet(self, som):
        if som not in self.sommets and isinstance(som,Sommet):
            self.sommets.append(som)

    def remove_sommet(self, som):
        if som in self.sommets:
            self.sommets.remove(som)

    def connect(self, som1, som2):
        if som1 in self.sommets and som2 in self.sommets:
            som1.connect(som2)

    def disconnect(self, som1, som2):
        if som1 in self.sommets and som2 in self.sommets:
            som1.disconnect(som2)

    def __repr__(self):
        return self.sommets.__repr__()
