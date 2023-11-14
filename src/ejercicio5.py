"""Ejercicio 3.3.5¶
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
1. Crea un conjunto pares que contenga los números pares del conjunto numeros.
2. Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de 
tres del conjunto numeros.
3. Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y 
guárdala en un conjunto llamado pares_y_multiplos_de_tres."""

def crear_conjunto_de_pares(numeros:set) -> set:
    numeros_pares = set()
    for i in numeros:
        if i % 2 == 0:
            numeros_pares.add(i)
    return numeros_pares

def crear_conjunto_multiplos_de_3(numeros:set) -> set:
    multiplos_de_3 = set()
    for i in numeros:
        if i % 3 == 0:
            multiplos_de_3.add(i)
    return multiplos_de_3

def calcular_interseccion_pares_y_multiplos_de_3(numeros_pares:set,multiplos_de_3:set) -> set:
    interseccion = numeros_pares & multiplos_de_3
    return interseccion

if __name__ == "__main__":
    #Entrada
    numeros = {1,2,3,4,5,6,7,8,9,10}
    #Procesamiento
    numeros_pares = crear_conjunto_de_pares(numeros)
    multiplos_de_3 = crear_conjunto_multiplos_de_3(numeros)
    interseccion = calcular_interseccion_pares_y_multiplos_de_3(numeros_pares,multiplos_de_3)
    #Salida
    print(f"{numeros_pares}")
    print(f"{multiplos_de_3}")
    print(f"{interseccion}")
    