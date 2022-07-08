'''
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

'''

import math

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Lungimea dreptunghiului este {self.lungime}, latimea este {self.latime} iar culoarea este {self.culoare}')

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


dreptunghi1 = Dreptunghi(6, 2, 'rosu')
dreptunghi1.descrie()
print(dreptunghi1.aria())
print(dreptunghi1.perimetrul())
dreptunghi1.schimba_culoarea('verde')
dreptunghi1.descrie()