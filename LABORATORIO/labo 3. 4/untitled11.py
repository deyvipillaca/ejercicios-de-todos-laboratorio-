def multiplicar_matriz_por_numero(matriz, numero):
    resultado = [[elemento * numero for elemento in fila] for fila in matriz]
    return resultado

# Definir una matriz de ejemplo
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definir el número por el cual multiplicar la matriz
numero = 2

# Multiplicar la matriz por el número
resultado_multiplicacion = multiplicar_matriz_por_numero(matriz_ejemplo, numero)

# Imprimir la matriz resultante
for fila in resultado_multiplicacion:
    print(fila)
