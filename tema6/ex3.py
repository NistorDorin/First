'''
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul se numeste {self.nume} {self.prenume} si are un salariu de {self.salariu} lei')

    def nume_complet(self):
        return self.nume + " " + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        salariu_an = 12 * self.salariu

    def marire_salariu(self, procent):
        salariu_nou = self.salariu + self.salariu * 0.33
        return salariu_nou


angajat1 = Angajat('Matei', 'Gheorghe', 2000)
angajat1.descrie()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.marire_salariu(0.2))