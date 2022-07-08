'''
clasa Elev
atribute: nume, prenume, cod matricol, note (tinem aici toate notele de la mate, romana, info)
constructor: nume, prenume, cod matricol
metode:
descrie elev
adauga nota per materie
afiseaza note per materie
afiseaza media per materie
afiseaza media generala anuala
'''

class Elev:
    nume = None
    prenume = None
    cod_matricol = None
    note = None

    def __init__(self, nume, prenume, cod_matricol):
        self.nume = nume
        self.prenume = prenume
        self.cod_matricol = cod_matricol
        self.note = dict()

    def printt(self):
        print(self.note.values())


    def descrie_elev(self):
        print(f"Pe elev il cheama {self.nume} {self.prenume}, "
              f"are cod matricol {self.cod_matricol} si are notele {self.note}")

    def adauga_nota_per_materie(self, materie, nota):
        if materie in self.note.keys():
            self.note[materie].append(nota)
        else:
            self.note[materie] = []
            self.note[materie].append(nota)

    def afiseaza_note_per_materie(self, materie):
        print(f'Notele la {materie}:', self.note[materie])

    def afiseaza_media_per_materie(self, materie):
        suma = 0
        for it in self.note[materie]:
            suma +=it
        media = suma / len(self.note[materie])
        print(media)

    def afiseaza_media_generala_anuala(self):
        suma = 0
        count = 0
        for xlist in self.note.values():
            for nota in xlist:
                count +=1
                suma +=nota
        media = suma/count
        print(media)



elev1 = Elev('Ionescu', 'Luci', 112)
elev1.descrie_elev()
elev1.adauga_nota_per_materie('informatica', 5)
elev1.adauga_nota_per_materie('informatica', 10)
elev1.adauga_nota_per_materie('informatica', 9)
elev1.adauga_nota_per_materie('romana', 7)
elev1.adauga_nota_per_materie('romana', 8)
elev1.adauga_nota_per_materie('romana', 8)
elev1.descrie_elev()
elev1.afiseaza_note_per_materie('romana')

elev1.afiseaza_media_per_materie('informatica')

elev1.afiseaza_media_generala_anuala()