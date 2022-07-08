# pentru un string afisati numarul de caractere mici, caractere mari, cifre si speciale

nr_caractere_mici = 0
nr_caractere_mari = 0
nr_cifre = 0
nr_caractere_speciale = 0

input_string = 'Curs de Python la adresa: @120.20.1'

for i in rage(0, len(input_string)):
    if input_string[i].isupper():
        nr_caractere_mari += nr_caractere_mari
    elif input_string[i].islower():
        nr_caractere_mici += nr_caractere_mici
    elif input_string[i].isdigit():
        nr_cifre += nr_cifre
    else:
        nr_caractere_speciale += nr_caractere_speciale

