# Crear una lista con nodos que contienen datos duplicados
lista_original = [1, 2, 3, 2, 4, 5, 3, 6]

# Eliminar nodos duplicados dejando solo una instancia de cada dato
lista_sin_duplicados = list(dict.fromkeys(lista_original))

# Imprimir la lista resultante hacia adelante
print("Lista sin nodos duplicados hacia adelante:", lista_sin_duplicados)

# Imprimir la lista resultante hacia atrás
print("Lista sin nodos duplicados hacia atrás:", lista_sin_duplicados[::-1])
