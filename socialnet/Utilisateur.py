from Sommet import Sommet


class Utilisateur(Sommet):

    def __init__(self, nom, prenom, age):
        Sommet.__init__(self, nom)
        self.prenom = prenom
        self.age = age

    def get_prenom(self):
        return self.prenom

    def get_age(self):
        return self.age

    def connect(self, som):
        Sommet.connect(self, som)

    def disconnect(self, som):
        Sommet.disconnect(self, som)

    def magie(self):
        res = ":" + "U" + ":" + self.nom + "," + self.prenom + "," + str(self.age)
        return res

    def __repr__(self):
        res = "<" + self.prenom + " " + self.nom + " " + str(self.age) + " out:["
        for i in self.out:
            if i == self.out[-1]:
                res += "<" + i.__str__() + ">"
            else:
                res += "<" + i.__str__() + "> ,"
        return res + "]>"

    def __str__(self):
        return self.prenom + " " + self.nom + " " + str(self.age)
