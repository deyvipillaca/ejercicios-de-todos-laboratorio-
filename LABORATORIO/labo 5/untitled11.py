def numeros_ordenados(conjunto_numeros):
    numeros_ordenados = sorted(conjunto_numeros)
    return set(numeros_ordenados)

# Ejemplo de uso
numeros = {5, 2, 8, 1, 3}
numeros_ordenados_menor_a_mayor = numeros_ordenados(numeros)

print("Números ordenados de menor a mayor:", numeros_ordenados_menor_a_mayor)
