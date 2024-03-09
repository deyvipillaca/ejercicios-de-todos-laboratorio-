import random

# Definir las dimensiones de la matriz
filas = 100
columnas = 100

# Crear una matriz de números aleatorios
matriz_aleatoria = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]

# Imprimir la matriz (solo se muestra una parte para no saturar la salida)
for i in range(5):  # Mostrar solo las primeras 5 filas
    print(matriz_aleatoria[i])
