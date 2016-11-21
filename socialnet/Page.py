from Sommet import Sommet
from Utilisateur import Utilisateur

class Page(Sommet):

    def __init__(self, nom):
        Sommet.__init__(self, nom)
        self.admins = []

    def get_admins(self):
        return self.admins

    def add_admin(self, admin):
        if admin not in self.admins and isinstance(admin, Utilisateur):
            self.admins.append(admin)

    def remove_admin(self, admin):
        if admin in self.admins:
            self.admins.remove(admin)

    def connect(self, som):
        print("A page cannot connect to anything")

    def disconnect(self, som):
        print("A page cannot disconnect to anything")

    def magie(self):
        res = ":" + "P" + ":" + self.nom
        return res

    def __repr__(self):
        res = "<" + self.nom + " admins:["
        for i in self.admins:
            if i == self.admins[-1]:
                res += "<" + i.__str__() + ">"
            else:
                res += "<" + i.__str__() + "> ,"
        return res + "]>"

    def __str__(self):
        return Sommet.__str__(self)
