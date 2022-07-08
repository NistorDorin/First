'''
# functie care sa returneze procentul ramas dintrun rezervor de benzina
# input: cantitate_ramasa, capacitate_rezervor
# daca procentul e sub 15% afisam un warning
'''

def benzina_ramasa(cantitate_ramasa, capacitate_rezervor):
    limita = 0.15 * capacitate_rezervor
    if cantitate_ramasa < limita:
        return 'Warning'
    else:
        return 'Nu trebuie alimentat'
