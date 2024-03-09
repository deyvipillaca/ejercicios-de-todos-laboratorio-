# Crear una lista con al menos 4 nodos
lista_original = [1, 2, 3, 4]

# Duplicar cada nodo de la lista
lista_duplicada = [item for item in lista_original for _ in range(2)]

# Imprimir la lista original hacia adelante
print("Lista original hacia adelante:", lista_original)

# Imprimir la lista original hacia atrás
print("Lista original hacia atrás:", lista_original[::-1])

# Imprimir la lista duplicada hacia adelante
print("Lista duplicada hacia adelante:", lista_duplicada)

# Imprimir la lista duplicada hacia atrás
print("Lista duplicada hacia atrás:", lista_duplicada[::-1])
