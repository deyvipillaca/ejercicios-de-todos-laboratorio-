def numeros_divisibles(conjunto_numeros, divisor):
    numeros_divisibles = set()
    for numero in conjunto_numeros:
        if numero % divisor == 0:
            numeros_divisibles.add(numero)
    return numeros_divisibles

# Ejemplo de uso
numeros = {10, 15, 20, 25, 30, 35}
divisor = 5
numeros_divisibles_por_5 = numeros_divisibles(numeros, divisor)

print(f"Números divisibles por {divisor}: {numeros_divisibles_por_5}")
