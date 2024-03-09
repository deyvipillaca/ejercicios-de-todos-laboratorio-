def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palabras_palindromas_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_filtradas = {palabra for palabra in conjunto_palabras if es_palindromo(palabra) and len(palabra) == longitud}
    palabras_filtradas_ordenadas = sorted(palabras_filtradas)
    return palabras_filtradas_ordenadas

# Ejemplo de uso
palabras = {"radar", "oso", "casa", "reconocer", "solos"}
longitud_deseada = 5
palabras_palindromas_longitud_ordenadas = palabras_palindromas_longitud_ordenadas(palabras, longitud_deseada)

print(f"Palabras palíndromas de longitud {longitud_deseada} ordenadas de menor a mayor:", palabras_palindromas_longitud_ordenadas)

