lista1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

lista_fara_zero = []
lista_zero = []

for i in range(0, len(lista1)):
    if lista1[i]==0:
        lista_zero.append(lista1[i])
    else:
        lista_fara_zero.append(lista1[i])
print(lista_zero)
print(lista_fara_zero)
lista_fara_zero.extend(lista_zero)
print(lista_fara_zero)