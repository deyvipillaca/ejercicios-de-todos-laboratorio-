def palabras_con_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_filtradas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    palabras_filtradas_ordenadas = sorted(palabras_filtradas)
    return palabras_filtradas_ordenadas

# Ejemplo de uso
palabras = {"casa", "perro", "gato", "oso", "elefante"}
longitud_deseada = 4
palabras_con_longitud_ordenadas = palabras_con_longitud_ordenadas(palabras, longitud_deseada)

print(f"Palabras de longitud {longitud_deseada} ordenadas de menor a mayor:", palabras_con_longitud_ordenadas)
