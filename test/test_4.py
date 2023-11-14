from src.ejercicio4 import devolver_frutas_comunes,devolver_frutas_unicas_en_conjunto1,devolver_frutas_unicas_en_conjunto2
import pytest

def test_devolver_frutas_comunes():
    frutas1 = {"manzana","pera","naranja","plátano","uva"}
    frutas2 = {"manzana","pera","durazno","sandía","uva"}
    assert devolver_frutas_comunes(frutas1,frutas2) == {"manzana","pera","uva"}

def test_devolver_frutas_unicas_en_conjunto1():
    frutas1 = {"manzana","pera","naranja","plátano","uva"}
    frutas2 = {"manzana","pera","durazno","sandía","uva"}
    assert devolver_frutas_unicas_en_conjunto1(frutas1,frutas2) == {"naranja","plátano"}

def test_devolver_frutas_unicas_en_conjunto2():
    frutas1 = {"manzana","pera","naranja","plátano","uva"}
    frutas2 = {"manzana","pera","durazno","sandía","uva"}
    assert devolver_frutas_unicas_en_conjunto2(frutas1,frutas2) == {"durazno","sandía"}

if __name__ == "__main__":
    pytest.main()