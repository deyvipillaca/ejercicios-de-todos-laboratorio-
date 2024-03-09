def diferencia_entre_conjuntos(conjunto1, conjunto2):
    diferencia = conjunto1.difference(conjunto2)
    return diferencia

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
numeros_en_conjunto1_no_en_conjunto2 = diferencia_entre_conjuntos(conjunto1, conjunto2)

print("Números en el primer conjunto pero no en el segundo:", numeros_en_conjunto1_no_en_conjunto2)

