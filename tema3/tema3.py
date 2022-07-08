note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

note_muzicale = note_muzicale[::-1]
print(note_muzicale)

note_muzicale.reverse()
print(note_muzicale)

print(note_muzicale.count('do'))

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

lista1.extend(lista2)
print(lista1)
lista12 = lista1 + lista2
print(lista12)

lista1.sort()
print(lista1)
# lista1.pop(0)
lista1.remove(0)
print(lista1)

if(len(lista1) != 0):
    print('Lista nu este goala')
else:
    print('Lista este goala')

lista1.clear()
print(lista1)

if(len(lista1) != 0):
    print('Lista nu este goala')
else:
    print('Lista este goala')

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.values())


print('Ana a luat nota', dict1['Ana'])
print('Gigel a luat nota', dict1['Gigel'])
print('Dore a luat nota', dict1['Dorel'])

dict2 = {'Dorel' : 6}
dict1.update(dict2)
print(dict1)

dict1.pop('Gigel')
print(dict1)

dict1.update({'Ionica': 9})
print(dict1)

zile_sapt = {'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)

if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor saptamanii")
else:
    print("Weekend nu este un subset al zilelor saptamanii")

res2 = zile_sapt.difference(weekend)
print(res2)

res = zile_sapt.intersection(weekend)
print(res)







