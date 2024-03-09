def encontrar_elemento_maximo(matriz):
    maximo = float('-inf')  # Inicializar el valor máximo como negativo infinito

    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento

    return maximo

# Definir una matriz de ejemplo
matriz_ejemplo = [
    [1, 5, 3],
    [9, 2, 7],
    [4, 8, 6]
]

# Encontrar el elemento máximo de la matriz
elemento_maximo = encontrar_elemento_maximo(matriz_ejemplo)

print("El elemento máximo de la matriz es:", elemento_maximo)
