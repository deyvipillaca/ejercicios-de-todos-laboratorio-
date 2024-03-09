def invertir_cadena_con_pila(cadena):
    pila = []
    for caracter in cadena:
        pila.append(caracter)

    cadena_invertida = ""
    while pila:
        cadena_invertida += pila.pop()

    return cadena_invertida

# Cadena original
cadena_original = "Hola Mundo!"

# Invertir el orden de los caracteres utilizando una pila
cadena_invertida = invertir_cadena_con_pila(cadena_original)

print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)


