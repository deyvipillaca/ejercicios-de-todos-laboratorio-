def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_ordenados(conjunto_numeros):
    numeros_primos = {numero for numero in conjunto_numeros if es_primo(numero)}
    numeros_primos_ordenados = sorted(numeros_primos)
    return numeros_primos_ordenados

# Ejemplo de uso
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_primos_ordenados = numeros_primos_ordenados(numeros)

print("Números primos ordenados de menor a mayor:", numeros_primos_ordenados)
