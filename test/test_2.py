from src.ejercicio2 import comprobar_nombres_repetidos_en_primaria_y_secundaria,comprobar_nombres_unicos_en_primaria,comprobar_nombres_de_primaria_incluidos_en_secundaria
import pytest

def test_comprobar_nombres_repetidos_en_primaria_y_secundaria():
    alumnos_primaria = {"alvaro ruiz","helena garcia","dario fernandez"}
    alumnos_secundaria = {"dario fernandez"}
    assert comprobar_nombres_repetidos_en_primaria_y_secundaria(alumnos_primaria,alumnos_secundaria) == {"dario fernandez"}

def test_comprobar_nombres_unicos_en_primaria():
    alumnos_primaria = {"alvaro ruiz","helena garcia","dario fernandez"}
    alumnos_secundaria = {"dario fernandez"}
    assert comprobar_nombres_unicos_en_primaria(alumnos_primaria,alumnos_secundaria) == {"alvaro ruiz","helena garcia"}

def test_comprobar_nombres_incluidos_en_secundaria_True():
    alumnos_primaria = {"Ismael Abad","Eloy Martos Cobos","Donald Trump"}
    alumnos_secundaria = {"Ismael Abad","Eloy Martos Cobos","Donald Trump","Juan Sevillano"}
    assert comprobar_nombres_de_primaria_incluidos_en_secundaria(alumnos_primaria,alumnos_secundaria) == True

def test_comprobar_nombres_incluidos_en_secundaria_False():
    alumnos_primaria = {"Ismael Abad","Eloy Martos Cobos","Donald Trump","Juan Sevillano"}
    alumnos_secundaria = {"Ismael Abad","Eloy Martos Cobos","Donald Trump"}
    assert comprobar_nombres_de_primaria_incluidos_en_secundaria(alumnos_primaria,alumnos_secundaria) == False


if __name__ == "__main__":
    pytest.main()