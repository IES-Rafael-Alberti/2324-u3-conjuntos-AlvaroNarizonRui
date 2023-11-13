"""
Ejercicio 3.3.2¶
Solicitar al usuario que introduzca los nombres de pila de los alumnos de 
primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, 
solicitar que introduzca los nombres de los alumnos de secundaria, finalizando 
al introducir “x”.

-Mostrar los nombres de todos los alumnos de primaria y los de secundaria, 
sin repeticiones.
-Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
-Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
-Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""

def comprobar_nombres_repetidos_en_primaria_y_secundaria(alumnos_primaria:set,alumnos_secundaria:set) -> set:
    nombres_comunes = alumnos_primaria & alumnos_secundaria
    return nombres_comunes

def comprobar_nombres_unicos_en_primaria(alumnos_primaria:set,alumnos_secundaria:set) -> set:
    nombres_unicos_primaria = alumnos_primaria - alumnos_secundaria
    return nombres_unicos_primaria

def comprobar_nombres_de_primaria_incluidos_en_secundaria(alumnos_primaria:set,alumnos_secundaria:set) -> bool:
    nombres_primaria_incluidos_en_secundaria = alumnos_primaria <= alumnos_secundaria
    return nombres_primaria_incluidos_en_secundaria

if __name__ == "__main__":
    alumnos_primaria = set()
    alumnos_secundaria = set()

    #Entrada
    final = False
    while final != True:
        entrada_primaria = input("Escribe los nombres de pila de los alumnos de primaria (X para terminar): ")
        if entrada_primaria.lower() == "x":
            final = True
        else:
            alumnos_primaria.add(entrada_primaria)
    final_2 = False
    while final_2 != True:
        entrada_secundaria = input("Escribe los nombres de pila de los alumnos de secundaria (X para terminar): ")
        if entrada_secundaria.lower() == "x":
            final_2 = True
        else:
            alumnos_secundaria.add(entrada_secundaria) 
    #Procesamiento
    nombres_repetidos_en_primaria_y_secundaria = comprobar_nombres_repetidos_en_primaria_y_secundaria(alumnos_primaria,alumnos_secundaria)
    nombres_unicos_en_primaria = comprobar_nombres_unicos_en_primaria(alumnos_primaria,alumnos_secundaria)
    comprobacion_nombres_incluidos_en_secundaria = comprobar_nombres_de_primaria_incluidos_en_secundaria(alumnos_primaria,alumnos_secundaria)

    #Salida
    print(f"Los nombres repetidos en primaria y secundaria son : {nombres_repetidos_en_primaria_y_secundaria}")
    print(f"Los nombres únicos en primaria son {nombres_unicos_en_primaria}")
    if comprobacion_nombres_incluidos_en_secundaria != False:
        print("Todos los alumnos de primaria están incluidos en secundaria")
    else:
        print("No están incluidos todos los alumnos de primaria en secundaria")