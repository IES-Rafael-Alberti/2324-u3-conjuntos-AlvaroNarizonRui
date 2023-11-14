"""Ejercicio 3.3.6¶
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

1. Crea un conjunto consonantes que contenga las letras del alfabeto que no 
son vocales.
2. Crea un conjunto letras_comunes que contenga las letras que están tanto 
en el conjunto vocales como en el conjunto consonantes."""

def crear_conjunto_consonantes(vocales:set) -> set:
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    consonantes = alfabeto - vocales
    return consonantes

def crear_conjunto_letras_comunes(vocales:set,consonantes:set) -> set:
    letras_comunes = consonantes & vocales
    return letras_comunes

if __name__ == "__main__":
    #Entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    #Procesamiento
    consonantes = crear_conjunto_consonantes(vocales)
    letras_comunes = crear_conjunto_letras_comunes(vocales,consonantes)
    #Salida
    print(f"{consonantes}")
    print(f"{letras_comunes}")