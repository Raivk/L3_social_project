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
            for duo in self.get_arcs():
                if duo[1] == som:
                    duo[0].disconnect(som)
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

    def save(self):
        sommets_fic = {}
        fichier = open("lasauvegardedelamortquitue.stylux", "w")
        i = 0
        for sommet in self.sommets:
            fichier.write(str(i) + sommet.magie() + "\n") #tous les sommets
            sommets_fic[i] = sommet
            i = i + 1
        fichier.write("---\n")
        for idf in sommets_fic.keys():
            sommet = sommets_fic.get(idf)
            for id2 in sommets_fic.keys():
                sommet2 = sommets_fic.get(id2)
                if sommet2 in sommet.get_connections():
                    fichier.write("[" + str(idf) + "," + str(id2) + "]\n" ) #1 suit 2
        fichier.write("---\n")
        for idf in sommets_fic.keys():
            sommet = sommets_fic.get(idf)
            if isinstance(sommet, Page):
                if sommet.get_admins() != None:
                    admins = sommet.get_admins()
                    for possible in sommets_fic:
                        if sommets_fic.get(possible) in admins:
                            fichier.write("[" + str(idf) + "," + str(possible) + "]") #page, admin

        fichier.close()


        fichier.close()

    def ouv(self, path):
        fichier = open(path, "r")
        #for ligne in fichier.read():
        #    test
        fichier.close()
    def __repr__(self):
        res = "["
        for i in self.sommets:
            if i == self.sommets[-1]:
                res += i.__repr__()
            else:
                res += i.__repr__() + " , "
        return res + "]"