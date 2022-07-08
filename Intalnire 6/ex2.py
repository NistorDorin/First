'''
clasa Caine
atribute - rasa, nume, culoare, nume_stapan, varsta
metode:
descrie() - afisam nume, nume_stapan, rasa si culoarea intr-un mesaj coerent)
calculator_varsta() - afisam varsta in ani cainesti (x7)
la_multi_ani() - cainele creste 1 an
latra() - afisam '{nume}: Ham Ham' (cand apelam latra(), vom afisa random ham, ham ham sau ham ham ham) hint 'ham ' * n

creati 2 obiecte de tip Caine cu atribute diferite
apelati descrie pt fiecare
apelati latra pt fiecare
afisati varsta in ani cainesti
t
'''
import random

class Caine:
    # atribute
    rasa = None
    nume = None
    culoare = None
    nume_stapan = None
    varsta = None

    # constructor
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def descrie(self):
        print(f'Pe catel il cheama {self.nume}, '
              f'pe stapan {self.nume_stapan},'
              f' este de rasa {self.rasa} si '
              f'este de culoare {self.culoare}')

    def calculator_varsta(self):
        self.varsta *= 7
        print(f"Varsta catelului {self.nume} este de {self.varsta} ani")

    def la_multi_ani(self):
        self.varsta +=1

    def latra(self):
        nr_ham = random.randint(1,4)
        print(f'{self.nume}:', nr_ham * 'Ham')

caine1 = Caine('Azorel', 3)
caine1.descrie()
caine1.latra()
caine1.calculator_varsta()
caine1.la_multi_ani()
caine1.calculator_varsta()

caine2 = Caine('Zorica', 2)
caine2.descrie()
caine2.latra()
caine2.calculator_varsta()
caine2.la_multi_ani()
caine2.calculator_varsta()