
from models.libro import Libro


def promedio_paginas(libros: list[Libro]):
    """Calcula el promedio de páginas de todos los libros."""
    if len(libros) == 0:
        return 0

    total_paginas = 0

    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)


def contar_libros(libros: list[Libro]):
    """Retorna la cantidad total de libros."""
    return len(libros)


def mostrar_disponibles(lista_libros: list[Libro]):
    """Muestra solo los libros que están disponibles."""
    encontrados = 0

    print("\n=== LIBROS DISPONIBLES ===")

    for libro in lista_libros:
        if libro["disponible"] is True:
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Páginas: {libro['paginas']}")
            print("-" * 30)
            encontrados += 1

    if encontrados == 0:
        print("No hay libros disponibles.")


def buscar_por_paginas(
    lista_libros: list[Libro], max_paginas: int
):
    """Muestra libros con menos páginas que max_paginas."""
    encontrados = 0

    print(f"\n=== LIBROS CON MENOS DE {max_paginas} PÁGINAS ===")

    for libro in lista_libros:
        if libro["paginas"] < max_paginas:
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Páginas: {libro['paginas']}")
            print("-" * 30)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron libros con esa cantidad de páginas.")


def agregar_categoria(
    set_categorias: set[str], nueva_categoria: str
):
    """Agrega una nueva categoría al conjunto."""
    nueva_categoria = nueva_categoria.strip()

    if nueva_categoria:
        set_categorias.add(nueva_categoria)
        print(f"Categoría '{nueva_categoria}' agregada al conjunto.")
        print("Categorías actuales:", sorted(set_categorias))
    else:
        print("Error: la categoría no puede estar vacía.")
