# biblioteca_virtual.py

# Lista que almacenará los libros
biblioteca = []

# 1. Agrega libros con títulos usando *args
def agregar_libros(*titulos):
    for titulo in titulos:
        libro = {"titulo": titulo, "autor": None, "genero": None, "año": None}
        biblioteca.append(libro)

# 2. Asigna o actualiza detalles de un libro existente
def asignar_detalles(titulo, autor, genero, año):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            libro["autor"] = autor
            libro["genero"] = genero
            libro["año"] = año
            break
    else:
        print(f"No se encontró el libro '{titulo}' en la biblioteca.")

# 3. Muestra todos los libros registrados
def mostrar_biblioteca():
    if not biblioteca:
        print("La biblioteca está vacía.")
    else:
        print("Biblioteca Virtual:")
        for libro in biblioteca:
            print(f"- Título: {libro['titulo']}")
            print(f"  Autor: {libro['autor']}")
            print(f"  Género: {libro['genero']}")
            print(f"  Año: {libro['año']}")
            print("")

# 4. Busca libros según los filtros dados con **kwargs
def buscar_libros(**filtros):
    resultados = biblioteca
    if "genero" in filtros:
        resultados = [libro for libro in resultados if libro["genero"] == filtros["genero"]]
    if "autor" in filtros:
        resultados = [libro for libro in resultados if libro["autor"] == filtros["autor"]]
    if "año_max" in filtros:
        resultados = [libro for libro in resultados if libro["año"] is not None and libro["año"] <= filtros["año_max"]]

    if resultados:
        print("Resultados de la búsqueda:")
        for libro in resultados:
            print(f"- {libro['titulo']} ({libro['año']}) - {libro['autor']} [{libro['genero']}]")
    else:
        print("No se encontraron libros con esos criterios.")

# Ejemplo de uso
if __name__ == "__main__":
    agregar_libros("Cien años de soledad", "El principito", "Don Quijote")
    asignar_detalles("El principito", "Antoine de Saint-Exupéry", "Ficción", 1943)
    asignar_detalles("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967)
    asignar_detalles("Don Quijote", "Miguel de Cervantes", "Novela", 1605)

    mostrar_biblioteca()
    buscar_libros(genero="Ficción", año_max=2000)
