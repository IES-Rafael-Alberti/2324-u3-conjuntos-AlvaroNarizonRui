from src.ejercicio5 import crear_conjunto_de_pares,crear_conjunto_multiplos_de_3,calcular_interseccion_pares_y_multiplos_de_3
import pytest

def test_conjunto_pares():
    numeros = {1,2,3,4,5,6,7,8,9,10}
    assert crear_conjunto_de_pares(numeros) == {2,4,6,8,10}

def test_conjunto_multiplos_de_3():
    numeros = {1,2,3,4,5,6,7,8,9,10}
    assert crear_conjunto_multiplos_de_3(numeros) == {9,3,6}

def test_interseccion_pares_y_multiplos_de_3():
    numeros = {1,2,3,4,5,6,7,8,9,10}
    numeros_pares = crear_conjunto_de_pares(numeros)
    multiplos_de_3 = crear_conjunto_multiplos_de_3(numeros)
    assert calcular_interseccion_pares_y_multiplos_de_3(numeros_pares,multiplos_de_3) == {6}

