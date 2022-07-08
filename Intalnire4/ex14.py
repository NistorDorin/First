'''
14.
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777
'''

numar = int(input("Alegeti un numar de la tastatura: "))
for i in range(numar+1):
    for j in range(i):
        print(i, end=" ")
    print(' ')