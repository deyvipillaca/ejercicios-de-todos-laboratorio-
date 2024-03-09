def elemento_central(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas % 2 != 0 and columnas % 2 != 0:  # Matriz con número impar de elementos
        centro_fila = filas // 2
        centro_columna = columnas // 2
        return matriz[centro_fila][centro_columna]
    else:  # Matriz con número par de elementos
        # Aquí puedes definir tu lógica para acceder al elemento central en caso de una matriz con número par de elementos
        return None

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento_central = elemento_central(matriz_ejemplo)
print("Elemento central:", elemento_central)
