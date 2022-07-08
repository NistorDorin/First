'''
9.
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

maxim = numere[0]
for i in range(1, len(numere)):
    if (numere[i] > maxim):
        maxim = numere[i]
print(maxim)