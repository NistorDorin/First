'''
functie calculare impozit masina:
input: centimetri_cubi, este_hibrid
daca e hibrid, e 10, altfel sunt 3 categorii de taxe:
mai mic de 1300: 70,
mai mic de 2300:160
peste 2300: 900
'''

def calculare_impozit_masina(centimetri_cubi, este_hibrid):
    if este_hibrid:
        return 10
    else:
        if centimetri_cubi < 1300:
            return 70
        elif centimetri_cubi < 2300:
            return 160
        else:
            return 900