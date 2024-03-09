# Ingreso de una lista de números por el usuario
numeros_ingresados = input("lista de números separados por espacios: ")
lista_numeros = [float(num) for num in numeros_ingresados.split()]

# Ordenar la lista de menor a mayor
lista_ordenada = sorted(lista_numeros)

# Mostrar la lista ordenada
print("Lista ordenada de menor a mayor:")
print(lista_ordenada)
