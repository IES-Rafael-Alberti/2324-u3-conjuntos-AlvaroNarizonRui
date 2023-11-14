from src.ejercicio6 import crear_conjunto_consonantes,crear_conjunto_letras_comunes
import pytest

def test_crear_conjunto_consonantes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    assert crear_conjunto_consonantes(vocales) == {'h', 'k', 'w', 'q', 'y', 'n', 'b', 'd', 'x', 'j', 't', 'l', 'm', 's', 'g', 'p', 'v', 'c', 'f', 'r', 'z'}

def test_crear_conjunto_letras_comunes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = crear_conjunto_consonantes(vocales)
    assert crear_conjunto_letras_comunes(vocales,consonantes) == set()

if __name__ == "__main__":
    pytest.main()