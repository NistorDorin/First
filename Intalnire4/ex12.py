'''

Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici

'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numar = 0
for pozitie_numar in range(0, len(alte_numere)):
    for pozitie_numar2 in range(pozitie_numar, len(alte_numere)):
        if alte_numere[pozitie_numar] > alte_numere[pozitie_numar2]:
            numar = alte_numere[pozitie_numar]
            alte_numere[pozitie_numar] = alte_numere[pozitie_numar2]
            alte_numere[pozitie_numar2] = numar
print(alte_numere)
