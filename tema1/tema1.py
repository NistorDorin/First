
'''
Exercitiul 1)
o variabila este un container de date in care sunt stocate diferite valori/tipuri de date
care se pot modifica pe parcursul executarii programului
'''


'''
2.
Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
string, int, float, bool
Valorile le alegeti voi dupa preferinte
'''

nume = 'Marian'
varsta = 30
inaltime = 1.85
vaccinat = True

'''
3.
Utilizat functia type pentru a verifica daca au tipul de date asteptat
'''

print(type(nume))
print(type(varsta))
print(type(inaltime))
print(type(vaccinat))

'''
4.
Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
Verificati tipul acesteia
'''

inaltime = round(inaltime)
print("Exericitiul 4")
print(type(inaltime))

'''
5.
folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
(rezolvati nepotrivirile de tip prin ce modalitate doriti)
'''

print('Numele utilizatorului este:', nume)
print('Varsta utilizatorului este: ' + str(varsta))
print(f'Inaltimea utilizatorului este: {inaltime}')
print(f'Este utilizatorului vaccinat: {vaccinat}')

'''
6.
citeste de la tastatura numele
citeste de la tastatura prenumele
afiseaza 'Numele complet are x caractere'
'''

numele = input('Numele este: ')
prenume = input('Prenumele este: ')

lungime_nume = len(numele)
lungime_prenume = len(prenume)
x = lungime_nume + lungime_prenume
print(f'Numele complet are {x} caractere')

'''
7.
citeste de la tastatura lungimea
citeste de la tastatura latimea
afiseaza 'Aria dreptunghiului este x'
'''

lungimea = int(input('Lungimea dreptunghiului este: '))
latimea = int(input('Latimea dreptunghiului este: '))
aria = lungimea * latimea
print(f'Aria dreptunghiului este {aria}')

'''
8. 
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''

prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('x = '))
print(prop[:-x])


'''
9.
acelasi string
declara un string nou care sa fie format din primele 5 caractere + ultimele 5
'''

prop2 = prop[:5] + prop[-5:]


'''
10.
acelasi string
afisati de cate ori apare cuvantul 'the'
'''

cuv = ' the '
nr_aparitii = prop.count(cuv)
print(f'Cuvantul {cuv} apare de {nr_aparitii} ori')

'''
11.
acelasi string
inlocuieste the cu THE peste tot
printeaza rezultatul
'''

prop = prop.replace('the', 'THE')
print(prop)


'''
12.
acelasi string
salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest '
'''

rock = prop.find("rock")
print(prop[0:rock])

'''
13. 
citeste de la tastatura un string
verifica daca primul si ultimul caracter sunt la fel
se va folosi un assert
atentie: se doreste ca programul sa fie case insensitive
'apA' e acceptat
'''

argument = input("Scrie stringul: ").lower()
assert argument[0] == argument[-1]

'''
14.
avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
'''

numere = '0123456789'
par = numere[0:9:2]
impar = numere[1:10:2]
print(par)
print(impar)

# SAU

# for i in range(len(numere)):
#     nr = int(numere[i])
#     if nr%2 == 0:
#         print("Numerele pare sunt " + numere[i])

 # for i in range(len(numere)):
 #     nr = int(numere[i])
 #     if nr%2 != 0:
 #         print("Numerele impare sunt " + numere[i])

'''
15. 
acelasi string de mai sus
folositi un assert ca sa verificati daca acest string contine doar numere
hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
poate gasim o functie ajutatoare
'''

assert numere.isdigit()

'''
16. 
citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc
'''

sir1 = input('Scrie string de dimensiune impara: ')
while(len(sir1)%2 == 0):
     sir1 = input('Ai scris un string de dimensiune para, mai incearca odata: ')
mijloc = round(len(sir1)/2)
print(sir1[mijloc])

'''
17.
Folosind assert, verificati daca un string este palindrom
'''

sir2 = 'aaaa'
assert sir2[:] == sir2[::-1]

'''
18.
folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pentru verificare
'''

x, y = input('Scrie sirul format din 2 cuvinte:' ).split()
print(x)
print(y)

'''
19. 
citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) 
capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
=> alAbAlA portocAla
'''


sir19 = 'alabala portocala'
first = sir19[0]
last = sir19[-1]
for i in range(1, len(sir19)-1):
    if sir19[i] == first:
        i = first.upper()
        x = sir19[1:len(sir19)-1].replace(first, i)
sir19 = first + x + last
print(sir19)

'''
20.
citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ****
'''

user = input('User: ')
password = input('Password: ')
for i in range(len(password)):
    password = password.replace(password[i], '*')
x = len(password)
print(f'Parola pt user {user} este {password} și are {x} caractere')

