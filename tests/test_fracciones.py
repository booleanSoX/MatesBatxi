from src.fracciones import descomponer_en_factores_primos, menor_que_zero, Fraccion
import pytest



f1 = Fraccion(100,100)

def test_descomponer_en_factores_primos():
    assert descomponer_en_factores_primos(f1) == {2: 2, 5: 2}
    assert descomponer_en_factores_primos(Fraccion(3,4)) == {2: 2}
    assert descomponer_en_factores_primos(Fraccion(1,6)) == {2: 1, 3:1}



