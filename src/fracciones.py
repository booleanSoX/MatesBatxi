from __future__ import annotations
from soupsieve.css_parser import FLG_IN_RANGE
from unicodedata import numeric


class Fraccion:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    # GETTER
    @property
    def get_denominador(self):
        return self.__denominador

    # SETTER
    @get_denominador.setter
    def denominador(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__denominador = nuevo_valor
        else:
            raise ValueError("El numerador debe ser un entero")

    @staticmethod
    def sum(f1: Fraccion, f2: Fraccion) -> Fraccion:
        pass


##def resolver_fracciones_con_diferentes_denominador(primera_fraccion, segunda_fraccion):
#Se divide en tres partes


#Paso numero 1 es descomponerlos en numeros primos


# Paso numero 2

# Paso numero 3

class menor_que_zero(Exception):
    """Excepción lanzada cuando el numero introducido es menor que 0"""
    pass


def is_divisible(num: int, num2: int) -> bool:
    return num % num2 == 0


def descomponer_en_factores_primos(fracccion: Fraccion):
    denominador = fracccion.get_denominador

    numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    resultado: dict[int, int] = {}
    pos = 0

    while denominador != 1:
        if is_divisible(denominador, numeros_primos[pos]):
            denominador = denominador // numeros_primos[pos]
            if numeros_primos[pos] not in resultado:
                resultado[numeros_primos[pos]] = 1
            else:
                resultado[numeros_primos[pos]] += 1
        else:
            pos += 1

    return resultado

