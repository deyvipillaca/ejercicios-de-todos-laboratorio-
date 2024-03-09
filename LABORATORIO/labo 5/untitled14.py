def numeros_no_duplicados(conjunto_numeros):
    numeros_unicos = set()
    duplicados = set()

    for numero in conjunto_numeros:
        if numero in numeros_unicos:
            duplicados.add(numero)
        else:
            numeros_unicos.add(numero)

    numeros_no_duplicados = numeros_unicos - duplicados

    return numeros_no_duplicados

# Ejemplo de uso
numeros = {1, 2, 3, 2, 4, 5, 3, 6}
numeros_no_duplicados_encontrados = numeros_no_duplicados(numeros)

print("Números no duplicados en el conjunto:", numeros_no_duplicados_encontrados)
