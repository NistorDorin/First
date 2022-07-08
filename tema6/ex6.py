'''
6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''


class Masina:
    marca = None
    model = None
    viteza_maxima = 200
    viteza_actuala = 20
    culoare = 'gri'
    culori_disponibile = {'rosu', 'verde', 'galben', 'albastru', 'alb'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        model = self.model
        viteza_maxima = self.viteza_maxima

    def descrie(self):
        print(
            f'Marca: {self.marca}, Model: {self.model}, viteza_maxima: {self.viteza_maxima}, viteza_actuala: {self.viteza_actuala}, culoare: {self.culoare}, inmatriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        comp = False
        for culoare1 in self.culori_disponibile:
            if culoare1 == culoare:
                comp = True
                break
            else:
                comp = False
        if comp == True:
            self.culoare = culoare
        else:
            print("Eroare")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("Eroare, viteza este mai mica decat 0")
        elif viteza >= 0 and viteza < self.viteza_maxima:
            self.viteza_actuala += viteza
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0


masina1 = Masina('Opel', 240)
masina1.descrie()
masina1.vopseste('rosu')
masina1.descrie()
masina1.accelereaza(30)
masina1.descrie()
masina1.franeaza()
masina1.descrie()