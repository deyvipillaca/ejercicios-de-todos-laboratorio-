def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def encontrar_anagramas(conjunto_palabras):
    anagramas = set()
    palabras_procesadas = set()

    for palabra in conjunto_palabras:
        if palabra in palabras_procesadas:
            continue

        anagrama_actual = {palabra}
        for otra_palabra in conjunto_palabras:
            if otra_palabra != palabra and son_anagramas(palabra, otra_palabra):
                anagrama_actual.add(otra_palabra)
                palabras_procesadas.add(otra_palabra)

        if len(anagrama_actual) > 1:
            anagramas.update(anagrama_actual)

    return anagramas

# Ejemplo de uso
palabras = {"roma", "amor", "perro", "roper", "casa", "saca"}
anagramas_encontrados = encontrar_anagramas(palabras)

print("Palabras que son anagramas entre sí:", anagramas_encontrados)

