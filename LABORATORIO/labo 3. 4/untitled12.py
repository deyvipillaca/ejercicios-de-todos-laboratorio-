def media_matriz(matriz):
    total_elementos = 0
    suma_elementos = 0

    for fila in matriz:
        for elemento in fila:
            suma_elementos += elemento
            total_elementos += 1

    media = suma_elementos / total_elementos
    return media

# Definir una matriz de ejemplo
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular la media de la matriz
media = media_matriz(matriz_ejemplo)

print("La media de la matriz es:", media)
