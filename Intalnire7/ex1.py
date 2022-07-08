import math
from abc import abstractmethod

class FormaGeometrica:

    @abstractmethod

    def aria(self):
        raise NotImplementedError

    def descriere(self):
        print('Cel mai probabil am colturi')

class Cerc(FormaGeometrica):
    __raza = None
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        a = math.pi * pow(self.__raza, 2)
        return a

class Dreptunghi(FormaGeometrica):
    __lungime = None
    __latime = None

    def __init__(self, lungime, latime):
        self.__lungime = lungime
        self.__latime = latime

    def aria(self):
        a = self.__latime * self.__lungime
        return a