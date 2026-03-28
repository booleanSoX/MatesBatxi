from src.fracciones import descomponer_en_factores_primos, menor_que_zero
import pytest

print(descomponer_en_factores_primos(1000))

def test_descomponer_en_factores_primos():
    assert descomponer_en_factores_primos(100) == ['2/2', '5/2']
    with pytest.raises(menor_que_zero):
        descomponer_en_factores_primos(-6)


