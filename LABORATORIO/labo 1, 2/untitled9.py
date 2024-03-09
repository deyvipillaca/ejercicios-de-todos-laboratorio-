def contar_vocales(cadena):
    """
    Cuenta el número de vocales en una cadena de texto.
    """
    vocales = "aeiouAEIOU"
    contador = 0

    for caracter in cadena:
        if caracter in vocales:
            contador += 1

    return contador

# Ingreso de una cadena por el usuario
cadena_ingresada = input("Ingrese una cadena de texto: ")

# Conteo y resultado
numero_vocales = contar_vocales(cadena_ingresada)
print(f"El número de vocales en la cadena es: {numero_vocales}")

