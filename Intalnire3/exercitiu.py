sample_list = [{},{},{}]
sample_list2 = [{1, 2}, {}, {}]

lista_este_goala = True

for i in range(0, len(sample_list)):
    if len(sample_list[i]) != 0:
        lista_este_goala = False
    else:
        lista_este_goala = True

print(lista_este_goala)