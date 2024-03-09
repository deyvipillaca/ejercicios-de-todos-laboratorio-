def invertir_cadena(cadena):
    """
    Invierte una cadena de texto.
    """
    cadena_invertida = cadena[::-1]
    return cadena_invertida

# Ingreso de una cadena por el usuario
cadena_ingresada = input("Ingrese una cadena de texto: ")

# Inversión y resultado
cadena_invertida = invertir_cadena(cadena_ingresada)
print(f"Cadena original: {cadena_ingresada}")
print(f"Cadena invertida: {cadena_invertida}")

