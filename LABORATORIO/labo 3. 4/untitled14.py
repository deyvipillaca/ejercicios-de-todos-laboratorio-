import numpy as np

# Definir una matriz de ejemplo
matriz_ejemplo = np.random.randint(1, 100, (5, 5))  # Matriz aleatoria de 5x5

# Calcular la media
media = np.mean(matriz_ejemplo)

# Calcular la mediana
mediana = np.median(matriz_ejemplo)

# Calcular la desviación estándar
desviacion_estandar = np.std(matriz_ejemplo)

print("Matriz:")
print(matriz_ejemplo)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación Estándar:", desviacion_estandar)

