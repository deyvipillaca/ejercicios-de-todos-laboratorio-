def es_palindromo(palabra):
    return palabra == palabra[::-1]

def encontrar_palindromos(conjunto_palabras):
    palindromos = set()
    for palabra in conjunto_palabras:
        if es_palindromo(palabra):
            palindromos.add(palabra)
    return palindromos

# Ejemplo de uso
palabras = {"reconocer", "oso", "casa", "radar", "solos"}
palindromos_encontrados = encontrar_palindromos(palabras)

print("Palabras que son palíndromos:", palindromos_encontrados)

