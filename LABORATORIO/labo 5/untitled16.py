def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palabras_palindromas_ordenadas(conjunto_palabras):
    palabras_palindromas = {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}
    palabras_palindromas_ordenadas = sorted(palabras_palindromas)
    return palabras_palindromas_ordenadas

# Ejemplo de uso
palabras = {"radar", "oso", "casa", "reconocer", "solos"}
palabras_palindromas_ordenadas = palabras_palindromas_ordenadas(palabras)

print("Palabras palíndromas ordenadas de menor a mayor:", palabras_palindromas_ordenadas)
