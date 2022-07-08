'''
5.
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

masini_vechi = []
for it in range(len(masini)):
    if masini[it] == 'Lastun' or masini[it] == 'Trabant':
        masini_vechi.append(masini[it])
        masini[it] ='Tesla'
print(masini)
print(masini_vechi)
