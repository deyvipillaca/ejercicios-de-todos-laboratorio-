def diferencia_simetrica_entre_conjuntos(conjunto1, conjunto2):
    diferencia_simetrica = conjunto2.difference(conjunto1)
    return diferencia_simetrica

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
numeros_en_conjunto2_no_en_conjunto1 = diferencia_simetrica_entre_conjuntos(conjunto1, conjunto2)

print("Números en el segundo conjunto pero no en el primero:", numeros_en_conjunto2_no_en_conjunto1)
