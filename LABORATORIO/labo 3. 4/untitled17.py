import numpy as np

def matriz_covarianza(matriz1, matriz2):
    covarianza = np.cov(matriz1, matriz2, rowvar=False)
    return covarianza

# Definir dos matrices de ejemplo
matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Calcular la matriz de covarianza entre las dos matrices
matriz_cov = matriz_covarianza(matriz1, matriz2)

print("Matriz de Covarianza:")
print(matriz_cov)
