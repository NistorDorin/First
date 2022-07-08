'''
10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for i in range(len(numere)):
    if (numere[i] > 0):
        numere[i] = 0 - numere[i]

print(numere)