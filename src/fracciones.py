#Algoritmo para resolver una suma de fracciones
from unicodedata import numeric


##def resolver_fracciones_con_diferentes_denominador(primera_fraccion, segunda_fraccion):
#Se divide en tres partes
##f1 = primera_fraccion

##f2 = segunda_fraccion
#Paso numero 1 es descomponerlos en numeros primos


# Paso numero 2

# Paso numero 3

class menor_que_zero(Exception):
    """Excepción lanzada cuando el numero introducido es menor que 0"""
    pass


def descomponer_en_factores_primos(numero: int):
    if numero < 0:
        raise menor_que_zero("No se puede introducir un numero menor que 0.")

    numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    resultado = []
    i = 0

    #Y si es negativo?
    while numero != 1:
        if numero % numeros_primos[i] == 0:
            resultado.append(numeros_primos[i])
            numero = numero / numeros_primos[i]
        elif numero == numeros_primos[i]:
            resultado.append(numeros_primos[i])
            i += 1
        else:
            i += 1

    ##parsing
    limite = len(resultado)
    if limite > 1:
        resultado2 = []
        pos = 0
        while pos < limite:
            numero_repetido = resultado[pos]
            veces_repetido = 1
            print(pos + 300)
            while pos +1 < limite and numero_repetido == resultado[pos + 1]:
                veces_repetido += 1
                pos += 1
            print(pos + 100)
            resultado2.append(str(numero_repetido) + "/" + str(veces_repetido))
            pos += 1
            print (pos + 200)

        return resultado2

    return resultado
