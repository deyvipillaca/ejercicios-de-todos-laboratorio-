def numeros_comunes(conjunto1, conjunto2):
    numeros_comunes = conjunto1.intersection(conjunto2)
    return numeros_comunes

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
numeros_en_comun = numeros_comunes(conjunto1, conjunto2)

print("Números en común entre los conjuntos:", numeros_en_comun)

