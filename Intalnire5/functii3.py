'''

# functie care sa returneze elementele comune a 2 liste
def elemente_comune(lista1, lista2):
    comune =[]



    return  comune;
print(elemente_comune([1,2,3,4],[3,5,6])) #trebuie sa afiseze [3]

'''


def elemente_comune(lista1,lista2):
    comune = []
    for element in lista1:
        for element2 in lista2:
            if element == element2:
                comune.append(element)
    return comune