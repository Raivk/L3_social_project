class Sommet:

    def __init__(self, nom):
        self.nom = nom
        self.out = []

    def compare_degree(self):
        return len(self.get_connections())

    def get_nom(self):
        return self.nom

    def get_connections(self):
        return self.out

    def connect(self, som):
        if som != self and som not in self.out:
            self.out.append(som)

    def disconnect(self, som):
        if som in self.out:
            self.out.remove(som)

    def magie(self):
        return self.magie()

    def __str__(self):
        return self.get_nom()

    def __repr__(self):
        return "<" + self.get_nom() + " out : " + self.out.__repr__() + ">"
