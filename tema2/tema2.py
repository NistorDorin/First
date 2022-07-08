'''
1.
Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else

if - prima conditie este valida/invalida -> se trece la rezolvarea expresiei 1/expresiei dupa if
else - daca nu -> se trece la rezolvarea expresiei 2/expresia dupa else
'''


x = 4445

'''
2.
Verifica si afiseaza daca x este numar natural sau nu
'''

if x >= 0:
    print(f'{x} este numar natural')
else:
    print('f{x} nu este numar natural')

'''
3.
Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
'''

if x > 0:
    print(f'{x} este numar pozitiv')
elif x < 0:
    print(f'{x} este numar negativ')
else:
    print(f'{x} este numar neutru')

'''
4. 
Verifica si afiseaza daca x este intre -2 si 13
'''

if x > -2 and x < 13:
    print(f'{x} este intre -2 si 13')
else:
    print(f'{x} nu este intre -2 si 13')

'''
5. 
Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
'''

y = 3

if x-y<5:
    print(f'diferenta dintre {x} si {y} este mai mica decat 5')
else:
    print(f'diferenta dintre {x} si {y} nu este mai mica decat 5')

'''
6. 
Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
'''

if not x > 5 and x < 27:
    print(f'diferenta intre {x} si {y} nu este intre 5 si 27')
else:
    print(f'diferenta intre {x} si {y} este intre 5 si 27')

'''
7.
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
'''

if x == y:
    print(f'{x} este egal cu {y}')
else:
    print(f'{x} nu este egal cu {y}')

'''
8. 
X, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
'''

z = 2

if x == y and y == z:
    print('triughiul este echilateral')
elif x == y or x == z or y == z:
    print('triunghiul este isoscel')
else:
    print('triunghiul este oarecare')

'''
9. 
Citeste o litera de la tastatura
Verifica si afiseaza daca este vocala sau nu
'''

litera = input('introdu litera ')

if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print('litera este vocala')
else:
    print('litera nu este vocala')

'''
10.
Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''

nota = int(input('introdu nota: '))
if nota > 9:
    nota = 'A'
    print(nota)
elif nota > 8 and nota < 9:
    nota = 'B'
    print(nota)
elif nota > 7 and nota < 8:
    nota = 'C'
    print(nota)
elif nota > 6 and nota < 7:
    nota ='D'
    print(nota)
elif nota > 4 and nota < 6:
    nota = 'D'
    print(nota)
else:
    nota = 'F'
    print(nota)

'''
11.Verifica daca x are minim 4 cifre (x e int)
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

count = 0
for i in range(len(str(x))):
    count += 1

if count <= 4:
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')
'''    
12.
Verifica daca x are exact 6 cifre 
'''

if count == 6:
    print(f'{x} are 6 cifre')
else:
    print(f'{x} nu are 6 cifre')

'''
13.
Verifica daca x este numar par sau impar (x e int)
'''

if int(x)%2 == 0:
    print(f'{x} este par')
else:
    print(f'{x} este impar')
