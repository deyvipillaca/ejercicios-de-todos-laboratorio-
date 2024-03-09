def suma_matrices(matriz1, matriz2):
    # Obtener las dimensiones de ambas matrices
    filas1, columnas1 = len(matriz1), len(matriz1[0])
    filas2, columnas2 = len(matriz2), len(matriz2[0])

    # Crear una matriz resultado con las dimensiones adecuadas
    filas_max = max(filas1, filas2)
    columnas_max = max(columnas1, columnas2)
    resultado = [[0 for _ in range(columnas_max)] for _ in range(filas_max)]

    # Sumar las matrices elemento por elemento
    for i in range(filas1):
        for j in range(columnas1):
            resultado[i][j] += matriz1[i][j]

    for i in range(filas2):
        for j in range(columnas2):
            resultado[i][j] += matriz2[i][j]

    return resultado

# Ejemplo de uso
matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6, 7],
    [8, 9, 10]
]

resultado_suma = suma_matrices(matriz1, matriz2)
for fila in resultado_suma:
    print(fila)
