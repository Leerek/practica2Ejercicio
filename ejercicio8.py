import collections


def es_primo (num):
    if num > 1:   # si es mayor a 1
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False


diccionario = {}


print('Ingrese una palabra')

miString = str(input()).lower()

frecuencias = collections.Counter(miString)

print('===NUMEROS PRIMOS===')

for char in frecuencias.keys():
    if es_primo(frecuencias[char]):
        print(char, ':', frecuencias[char], ' | O | \n       =====')
    else:
        print(char, ':', frecuencias[char], ' | X | \n       =====')


