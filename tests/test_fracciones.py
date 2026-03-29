from src.fracciones import descomposicion_en_numeros_primos, menor_que_zero, Fraccion, mcm
import pytest



def test_descomponer_en_factores_primos():
    assert descomposicion_en_numeros_primos(Fraccion(100,100)) == {2: 2, 5: 2}
    assert descomposicion_en_numeros_primos(Fraccion(3,4)) == {2: 2}
    assert descomposicion_en_numeros_primos(Fraccion(1,6)) == {2: 1, 3:1}
def test_mcm():
    f1 = Fraccion(3, 4)
    f2 = Fraccion(1, 6)
    fracciones = [f1,f2]
    assert mcm(fracciones) == {2: 2, 3: 1}



