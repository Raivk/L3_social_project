from Utilisateur import Utilisateur
from Page import Page
from Sommet import Sommet
import operator


class Graphe:

    def __init__(self):
        self.sommets = []

    def get_sommets(self):
        return self.sommets

    def get_sommets_by_name(self):
        return sorted(self.sommets, key=operator.attrgetter('nom'))

    def get_sommets_by_degree(self):
        return sorted(self.sommets, key=lambda som:Sommet.compare_degree(som))

    def get_arcs(self):
        res = []
        for som in self.sommets:
            for som2 in som.out:
                res.append((som, som2))
        return res

    def destroy_som(self,som):
        if som in self.sommets:
            for duo in self.get_arcs():
                if duo[1] == som:
                    duo[0].disconnect(som)
            self.sommets.remove(som)

    def get_nb_util(self):
        total = 0
        for som in self.sommets:
            if isinstance(som, Utilisateur):
                total += 1
        return total

    def get_nb_page(self):
        total = 0
        for som in self.sommets:
            if isinstance(som, Page):
                total += 1
        return total

    def get_admins(self):
        res = []
        for som in self.sommets:
            if isinstance(som, Page):
                res.extend(som.get_admins())
        return res

    def get_moy_age(self):
        total = 0
        for som in self.sommets:
            if isinstance(som, Utilisateur):
                total+= som.get_age()
        return total / self.get_nb_util()

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

    def som_len(self):
        return len(self.sommets)

    def arc_len(self):
        total = 0
        for som in self.sommets:
            total += len(som.get_connections())
        return total

    def __repr__(self):
        return self.sommets.__repr__()
