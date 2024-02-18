import pytest
from src.factorial import factorial

def test_factorial_de_1():
    assert factorial(1) == 1

def test_factorial_no_enter():
    with pytest.raises(TypeError):
        factorial(3.5)
        
def test_factorial_negatiu():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_de_5_es_120():
    assert factorial(5) == 120



