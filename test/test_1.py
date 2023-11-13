from src.ejercicio1 import extraer_domicilios
import pytest

def test_extraer_domicilios():
    lista_clientes = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    assert extraer_domicilios(lista_clientes) == {'Mirasol 218', 'Calle Las Flores 355', 'La Mancha 761'}

if __name__ == "__main__":
    pytest.main()