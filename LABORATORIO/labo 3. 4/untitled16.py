def kadane(array):
    max_actual = max_global = array[0]

    for i in range(1, len(array)):
        max_actual = max(array[i], max_actual + array[i])
        max_global = max(max_global, max_actual)

    return max_global

def submatriz_mayor_suma(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    max_suma = float('-inf')

    for i in range(filas):
        temp = [0] * columnas
        for j in range(i, filas):
            for k in range(columnas):
                temp[k] += matriz[j][k]
            max_suma = max(max_suma, kadane(temp))

    return max_suma

# Definir una matriz de ejemplo
matriz_ejemplo = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

# Encontrar la submatriz de mayor suma
suma_maxima_submatriz = submatriz_mayor_suma(matriz_ejemplo)

print("La suma máxima de una submatriz es:", suma_maxima_submatriz)
