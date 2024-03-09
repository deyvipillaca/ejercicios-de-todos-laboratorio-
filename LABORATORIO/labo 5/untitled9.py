def palabras_con_longitud(conjunto_palabras, longitud):
    palabras_filtradas = set()
    for palabra in conjunto_palabras:
        if len(palabra) == longitud:
            palabras_filtradas.add(palabra)
    return palabras_filtradas

# Ejemplo de uso
palabras = {"casa", "perro", "gato", "oso", "elefante"}
longitud_deseada = 4
palabras_con_longitud_deseada = palabras_con_longitud(palabras, longitud_deseada)

print(f"Palabras con longitud {longitud_deseada}:", palabras_con_longitud_deseada)
