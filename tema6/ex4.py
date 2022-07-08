'''
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')

    def debitare_cont(self, suma):
        if suma > self.sold:
            print("Fonduri insuficiente")
        else:
            sold_nou = self.sold - suma
            return sold_nou

    def creditare_cont(self, suma):
        sold_nou = self.sold + suma
        return sold_nou

cont1 = Cont('RO33113', 'Mihai Adrian', 30)
cont1.afisare_sold()
print(cont1.debitare_cont(12))
print(cont1.creditare_cont(10))


