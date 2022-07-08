'''
1. Functie care sa calculeze si sa returneze suma a 2 numere
'''
import math


def suma(a, b):
    return a+b

# print(suma(3,4))

'''
2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
'''

def par_impar(numar):
    if numar%2 == 0:
        return True
    else:
        return False

# print(par_impar(3))

'''
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''

def numar_caractere():
    print(len('Nistor Dorin')-1)

# numar_caractere()

'''
4. Functie care returneaza aria dreptunghiului
'''

def aria_dreptunghiului(lungime, latime):
    return lungime*latime

# print(aria_dreptunghiului(6,2))

'''
5. Functie care returneaza aria cercului
'''

def aria_cercului(raza):
    return math.pi * pow(raza,2)

# print(aria_cercului(2))

'''
6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
'''

def gaseste_caracter(x, cuvant):
    if cuvant.count(x):
        return True
    else:
        return False

# print(gaseste_caracter('x', 'parametru'))

'''
7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y 
'''

def count_lower_upper(cuvant):
    majuscule, minuscule  = 0, 0
    for i in cuvant:
        if i.isupper():
            majuscule +=1
        else:
            minuscule +=1
    print(f'Nr de caractere lower case este {minuscule}')
    print(f'Nr de caractere upper case este {majuscule}')

# count_lower_upper('PrinTAdd')


'''
9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale
'''

def comparatie(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale')

# comparatie(6,6)

'''
10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
'''

def adaugare(x, t):
    if x in t:
        print('am adaugat numarul in set. Acesta exista deja')
        return True
    elif x not in t:
        print('nu am adaugat numarul nou in set')
        return False

# print(adaugare(3, {4, 5, 6, 7, 0}))

'''
11. Functie care primeste o luna din an si returneaza cate zile are acea luna
'''

def zile_luna(luna):
    switcher = {
        'ianuarie': 31,
        'februarie': 28,
        'martie': 31,
        'aprilie': 30,
        'mai': 31,
        'iunie': 30,
        'iulie': 31,
        'august': 31,
        'septembrie': 30,
        'octombrie': 31,
        'noiembrie': 31,
        'decembrie': 30,
    }
    return switcher.get(luna, "nothing")

print(zile_luna('septembrie'))

'''
12. Functie calculator care sa returneze 4 valori 
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

'''
