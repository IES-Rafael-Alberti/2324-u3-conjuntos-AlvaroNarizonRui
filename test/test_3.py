from src.ejercicio3 import calcular_conjunto_potencia
import pytest

def test_conjunto_potencia():
    assert calcular_conjunto_potencia({1,2,3}) == [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]

if __name__ == "__main__":
    pytest.main()