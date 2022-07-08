'''
5.
Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)


genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi

Produs | cantitate | pret bucata | Total
Telefon |      7       |       700       | 49000
'''

from datetime import date


class Factura:
    seria = 'FC'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def descrie(self):
        print(f'Numar factura: {self.numar}, nume produs: {self.nume_produs}, '
              f'cantitate: {self.cantitate}, pret_buc: {self.pret_buc}')

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret_buc):
        self.pret_buc = pret_buc

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        total = self.pret_buc * self.cantitate
        print(f'Factura seria {self.seria} , numar {self.numar}')
        astazi = date.today()
        print('Data:', today)
        print('| Produs  | Cantitate | Pret bucata | Total |')
        print('|{:^9}|{:^11}|{:^13}|{:^6}|'.format(self.nume_produs, self.cantitate, self.pret_buc, total))



        # print('| {:1} | {:^4} | {:>4} | {:<3} |'.format(*row))
        '''
        Produs | cantitate | pret bucata | Total
        Telefon | 7 | 700 | 49000
        '''



today = date.today()
print("Today date is: ", today)

factura1 = Factura(4334, 'inghetata', 4, 40)
# factura1.descrie()
# factura1.schimba_cantitatea(5)
# factura1.descrie()
# factura1.schimba_pretul(50)
# factura1.descrie()
# factura1.schimba_nume_produs('prajitura')
# factura1.descrie()
factura1.genereaza_factura()