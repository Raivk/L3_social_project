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

    def __repr__(self):
        return "<" + Sommet.__str__(self) + " admins : " + self.admins.__repr__() + ">"
