def numeros_ordenados_sin_duplicados(conjunto_numeros):
    numeros_ordenados = sorted(conjunto_numeros)
    numeros_sin_duplicados = list(dict.fromkeys(numeros_ordenados))
    return set(numeros_sin_duplicados)

# Ejemplo de uso
numeros = {5, 2, 8, 1, 3, 2, 5, 4}
numeros_ordenados_sin_duplicados = numeros_ordenados_sin_duplicados(numeros)

print("Números ordenados de menor a mayor y sin duplicados:", numeros_ordenados_sin_duplicados)
