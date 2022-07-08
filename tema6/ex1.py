'''
Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
1.
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute
Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''

import math

class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare} iar raza {self.raza}')

    def aria(self):
        return math.pow(self.raza, math.pi)

    def diametru(self):
        return self.raza*2

    def circumferinta(self):
        return math.pi*self.diametru()


cerc1 = Cerc(2, 'rosu')
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())
