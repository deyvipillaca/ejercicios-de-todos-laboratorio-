def palabras_con_letra_inicial(conjunto_palabras, letra):
    palabras_filtradas = set()
    for palabra in conjunto_palabras:
        if palabra.startswith(letra):
            palabras_filtradas.add(palabra)
    return palabras_filtradas

# Ejemplo de uso
palabras = {"manzana", "banana", "pera", "sandía", "uva"}
letra_inicial = "m"
palabras_filtradas = palabras_con_letra_inicial(palabras, letra_inicial)

print(f"Palabras que comienzan con la letra '{letra_inicial}': {palabras_filtradas}")
