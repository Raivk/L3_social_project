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

    def __repr__(self):
        return "<" + self.prenom + " " + str(self.age) + " " + Sommet.__str__(self) + ">"
