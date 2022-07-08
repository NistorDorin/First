'''
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
a)‘Masina mea preferata este x’
b) Faceti acelasi lucru cu un for each
c) Faceti acelasi lucru cu un while

'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# a)
for it in range(len(masini)):
    print(f'Masina mea preferata este {masini[it]}')

# b)
for it in masini:
     print(f'Masina mea preferata este {it}')

# c)

var = 0
while var<len(masini):
    print(f'Masina mea preferata este {masini[var]}')
    var +=1

