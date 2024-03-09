# Crear una lista con al menos 9 nodos
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Contar cuántos nodos tienen un dato par y cuántos tienen un dato impar
pares = sum(1 for num in lista_original if num % 2 == 0)
impares = len(lista_original) - pares

# Imprimir la cantidad de nodos pares e impares
print("Cantidad de nodos con datos pares:", pares)
print("Cantidad de nodos con datos impares:", impares)

# Imprimir la lista original hacia adelante
print("Lista original hacia adelante:", lista_original)

# Imprimir la lista original hacia atrás
print("Lista original hacia atrás:", lista_original[::-1])
