from abc import ABCMeta


class Sommet:
    __metaclass__ = ABCMeta

    def __init__(self, n, t):
        self.name = n
        self.type = t
        self.out = []

