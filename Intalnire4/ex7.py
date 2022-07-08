'''
7.
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)

'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

count = 0
for numar in numere:
    if numar == 3:
        count +=1
print(count)