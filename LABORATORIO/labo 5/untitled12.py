def numeros_ordenados_mayor_a_menor(conjunto_numeros):
    numeros_ordenados = sorted(conjunto_numeros, reverse=True)
    return set(numeros_ordenados)

# Ejemplo de uso
numeros = {5, 2, 8, 1, 3}
numeros_ordenados_mayor_a_menor = numeros_ordenados_mayor_a_menor(numeros)

print("Números ordenados de mayor a menor:", numeros_ordenados_mayor_a_menor)
