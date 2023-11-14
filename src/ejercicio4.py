"""
Ejercicio 3.3.4¶
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

1. Crea conjuntos a partir de estas listas y nómbralos set_frutas1 
y set_frutas2.
2. Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
3. Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
4. Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""
def devolver_frutas_comunes(set_frutas1:set,set_frutas2:set) -> set:
    frutas_comunes = set_frutas1 & set_frutas2
    return frutas_comunes

def devolver_frutas_unicas_en_conjunto1(set_frutas1:set,set_frutas2:set) -> set:
    frutas_unicas_en_frutas1 = set_frutas1 - set_frutas2
    return frutas_unicas_en_frutas1

def devolver_frutas_unicas_en_conjunto2(set_frutas1:set,set_frutas2:set) -> set:
    frutas_unicas_en_frutas2 = set_frutas2 - set_frutas1
    return frutas_unicas_en_frutas2

if __name__ == "__main__":
    #Entrada
    frutas1 = ["manzana","pera","naranja","plátano","uva"]
    frutas2 = ["manzana","pera","durazno","sandía","uva"]
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)
    #Procesamiento
    frutas_comunes = devolver_frutas_comunes(set_frutas1,set_frutas2)
    frutas_unicas_1 = devolver_frutas_unicas_en_conjunto1(set_frutas1,set_frutas2)
    frutas_unicas_2 = devolver_frutas_unicas_en_conjunto2(set_frutas1,set_frutas2)
    #Salida
    print(f"frutas comunes : {frutas_comunes}")
    print(f"frutas unicas en el conjunto 1 : {frutas_unicas_1}")
    print(f"frutas unicas en el conjunto 2 : {frutas_unicas_2}")