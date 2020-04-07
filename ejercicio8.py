import collections


def es_primo (num): #un profe me mando un ejemplo mas eficiente para saber si el numero es primo
    if num > 1:   # si es mayor a 1
        for i in range(2, num):
            if (num % i) == 0:
                return False  # aca en el ejemplo que me mandaron habia un break pero no me gustaba y no es como estaba trabajando 
        return True           #el enunciado asi que lo cambie
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


