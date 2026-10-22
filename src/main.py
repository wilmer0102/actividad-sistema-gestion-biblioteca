
from data.biblioteca import libros, categorias
from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    contar_libros,
    promedio_paginas,
    agregar_categoria,
)


def mostrar_menu():
    print("\n========== SISTEMA DE BIBLIOTECA ==========")
    print("1. Ver libros disponibles")
    print("2. Buscar libros por cantidad de páginas")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")
    print("===========================================")


continuar = True

while continuar:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        mostrar_disponibles(libros)

    elif opcion == "2":
        try:
            max_paginas = int(
                input("Introduce el máximo de páginas: ")
            )

            if max_paginas <= 0:
                print("Introduce un número mayor que cero.")
            else:
                buscar_por_paginas(libros, max_paginas)

        except ValueError:
            print("Error: debes introducir un número entero.")

    elif opcion == "3":
        print("\n========== ESTADÍSTICAS ==========")
        print(f"Cantidad total de libros: {contar_libros(libros)}")

        if libros:
            promedio = promedio_paginas(libros)
            print(f"Promedio de páginas: {promedio:.2f}")
        else:
            print("No hay libros para calcular el promedio.")

    elif opcion == "4":
        nueva_categoria = input(
            "Escribe el nombre de la nueva categoría: "
        )
        agregar_categoria(categorias, nueva_categoria)

    elif opcion == "5":
        print("Gracias por utilizar el sistema de biblioteca.")
        continuar = False

    else:
        print("Opción no válida. Selecciona del 1 al 5.")
