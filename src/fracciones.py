from __future__ import annotations


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

    def __str__(self):
        return f"{self.__numerador}/{self.__denominador}"

    __repr__ = __str__


##def resolver_fracciones_con_diferentes_denominador(primera_fraccion, segunda_fraccion):
#Se divide en tres partes


#Paso numero 1 es descomponerlos en numeros primos


# Paso numero 2

# Paso numero 3

class menor_que_zero(Exception):
    """Excepción lanzada cuando el número introducido es menor que 0"""
    pass

#Funcion auxiliar
def is_divisible(num: int, num2: int) -> bool:
    return num % num2 == 0

#Esta función lo que hace dado un objeto de la clase Fraccion, devuelve en un diccionario los factores primos COMO LLAVES que se
#han necesitado para descomponerlo en 1, y devuelve la cantidad de veces que han sido necesarios como VALORES.
def descomposicion_en_numeros_primos(fracccion: Fraccion) -> dict[int,int]:
    #Cogemos el denominador
    denominador = fracccion.get_denominador

    #lista de numeros primos del 1 - 100, luego puedo hacer como un atributo de clase o global, para poder reutilizarlo
    numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


    resultado: dict[int, int] = {}
    pos = 0


    #Logica del código:
    #Hasta que el denominador no sea 1, quiero que vayas probando desde la primera posicion de los numeros primos
        #si el número es divisible entre ese número primo
            #quiero que dividas ese número entre el número primo
                #si no está, el número en la lista, añadelo
                #si esta, incrementamos la potencia porque el factor primo se repite en la descomposición
        #si no es divisible quiero que vayas a la siguiente posicion del número primo

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



#Funciona que recoge la lista de diccionarios en la que varios valores de factores primos descompuestos han sido añadidos
#Devuelve un diccionario recogiendo solamente las únicas y si son repetidas, el que tenga mayor exponente
#En este caso el valor del diccionario
#
def mcm(fracciones: list[Fraccion]) -> dict[int,int]:
    numeros_unicos = {}

    #EJ: Fracciones =
    for fraccion in fracciones:
        desfactorizado = descomposicion_en_numeros_primos(fraccion)

        for nuevo_valor in desfactorizado:
            if nuevo_valor not in numeros_unicos:
                numeros_unicos[nuevo_valor] = desfactorizado[nuevo_valor]
            elif desfactorizado[nuevo_valor] > numeros_unicos[nuevo_valor]:
                numeros_unicos[nuevo_valor] = desfactorizado[nuevo_valor]

    return numeros_unicos





def multiplicar(lista_fracciones : dict[int,int]) -> int:
    numeros_unicos = lista_fracciones
    resultado = 1
    enteros = []
    for numero in numeros_unicos:
        enteros.append(numero ** numeros_unicos[numero])

    for entero in enteros:
        resultado = entero * resultado
    return resultado


