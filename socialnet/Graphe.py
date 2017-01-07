from Utilisateur import Utilisateur
from Page import Page
from Sommet import Sommet

from socialnet.pyplotManager import PyplotManager
import time

import operator


class Graphe:

    def __init__(self):
        self.sommets = []
        self.pm = None

    def affiche(self):
        if self.pm == None:
            print('la')
            self.pm = PyplotManager(self)
            self.pm.prepa(self)
            self.pm.affiche(self)
        else:
            self.pm.refresh(self)
        print(self)

    def get_sommets(self):
        return self.sommets

    def get_pages(self):
        res = []
        for som in self.sommets:
            if isinstance(som, Page):
                res.append(som)
        return res

    def get_utils(self):
        res = []
        for som in self.sommets:
            if isinstance(som, Utilisateur):
                res.append(som)
        return res

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

    def get_arcs_admins(self):
        res = []
        for som in self.sommets:
            if isinstance(som,Page):
                for som2 in som.admins:
                    res.append((som, som2))
        return res

    def find_name(self,name):
        for som in self.sommets:
            if som.nom == name:
                return som
        print("Pas de sommet trouve pour le nom '" + name + "' !")
        return False

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
            if not isinstance(som, Page):
                for duo in self.get_arcs_admins():
                    if duo[1] == som:
                        duo[0].remove_admin(som)
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

    def page_rank(self):
        res = {}
        for som in self.sommets:
            res[som] = 1
        i = 0
        while i <= 100:
            for som in self.sommets:
                tempPr = 0
                for som2 in self.sommets:
                    if som in som2.out:
                        tempPr += (res[som2] / float(len(som2.out)))
                res[som] = (0.15 / float(len(self.sommets))) + (0.85 * tempPr)
            i += 1
        return res

    def plus_courte_distance(self, source):
        res = {}
        for som in self.sommets:
            if som == source:
                res[som] = 0
            else:
                res[som] = 10000000
        copy = res.keys()
        while len(copy) != 0:
            found = copy[0]
            min = res[found]
            for som in copy:
                if res[som] < min:
                    min = res[som]
                    found = som
            copy.remove(found)
            for som2 in found.out:
                alt = res[found] + 1
                if alt <= res[som2]:
                    res[som2] = alt
        return res

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
            toWrite = str(idf) + ":"
            sommet = sommets_fic.get(idf)
            wrote = False
            for id2 in sommets_fic.keys():
                sommet2 = sommets_fic.get(id2)
                if sommet2 in sommet.get_connections():
                    if not wrote:
                        toWrite += str(id2)  # 1 suit 2
                    else:
                        toWrite += "," + str(id2)  # 1 suit 2
                    wrote = True;
                    #fichier.write(str(idf) + "," + str(id2) + "\n")  #1 suit 2
            if wrote:
                fichier.write(toWrite + "\n")

        fichier.write("---\n")
        for idf in sommets_fic.keys():
            sommet = sommets_fic.get(idf)
            if isinstance(sommet, Page):
                if sommet.get_admins() != None:
                    toWrite = str(idf) + ":"
                    admins = sommet.get_admins()
                    wrote = False
                    for possible in sommets_fic:
                        if sommets_fic.get(possible) in admins:
                            if not wrote:
                                toWrite += str(possible)  # 1 possede 2 en admin
                            else:
                                toWrite += "," + str(possible)  # 1 possede 2 en admin
                            wrote = True
                            #fichier.write(str(idf) + "," + str(possible)) #page, admin
                    if wrote:
                        fichier.write(toWrite + "\n")

        fichier.close()

    def ouv(self, path):
        fichier = open(path, "r")
        i = 0
        somm = {}
        for ligne in fichier.readlines():
            ligne = ligne.replace("\n", "")
            if ligne == "---":
                i = i + 1
            else:
                if i == 0:
                    str = ligne.split(":")
                    if str[1] == "U":
                        carac = str[2].split(",")
                        somm[str[0]] = Utilisateur(carac[0], carac[1], int(carac[2]))
                        self.add_sommet(somm[str[0]])
                    if str[1] == "P":
                        somm[str[0]] = Page(str[2])
                        self.add_sommet(somm[str[0]])
                if i == 1:
                    firstUtil = ligne.split(":")[0]
                    others = ligne.split(":")[1].split(",")
                    for followed in others:
                        somm[firstUtil].connect(somm[followed])
                if i == 2:
                    thePage = ligne.split(":")[0]
                    theAdmins = ligne.split(":")[1].split(",")
                    for admin in theAdmins:
                        somm[thePage].add_admin(somm[admin])
        fichier.close()

    def __repr__(self):
        res = "["
        for i in self.sommets:
            if i == self.sommets[-1]:
                res += i.__repr__()
            else:
                res += i.__repr__() + " , "
        return res + "]"