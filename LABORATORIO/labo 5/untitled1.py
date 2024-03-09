def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos(conjunto_numeros):
    primos = set()
    for numero in conjunto_numeros:
        if es_primo(numero):
            primos.add(numero)
    return primos

# Ejemplo de uso
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
primos = numeros_primos(numeros)

print("Números primos en el conjunto:", primos)
