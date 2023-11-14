"""Ejercicio 3.3.3¶
El conjunto potencia de un conjunto S es el conjunto de todos
los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como 
parámetro un conjunto cualquiera s y retorne su 
«lista potencia» (la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), 
set([6, 4]), set([1, 4]), set([6, 1, 4])]"""

def calcular_conjunto_potencia(conjunto_s:set) -> list:
    elementos = list(conjunto_s)
    conjunto_potencia = [set()]

    for i in elementos:
        nuevos_subconjuntos = []
        for j in conjunto_potencia:
            nuevos_subconjuntos.append(j | {i})
        conjunto_potencia.extend(nuevos_subconjuntos)
    return conjunto_potencia



if __name__ == "__main__":
    #Entrada
    conjunto_s = {1,2,3}
    #Procesamiento
    conjunto_potencia = calcular_conjunto_potencia(conjunto_s)
    #Salida
    print(f"{conjunto_potencia}")