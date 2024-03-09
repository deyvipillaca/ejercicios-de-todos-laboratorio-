def numeros_duplicados(conjunto_numeros):
    numeros_unicos = set()
    duplicados = set()

    for numero in conjunto_numeros:
        if numero in numeros_unicos:
            duplicados.add(numero)
        else:
            numeros_unicos.add(numero)

    return duplicados

# Ejemplo de uso
numeros = {1, 2, 3, 2, 4, 5, 3, 6}
numeros_duplicados_encontrados = numeros_duplicados(numeros)

print("Números duplicados en el conjunto:", numeros_duplicados_encontrados)
