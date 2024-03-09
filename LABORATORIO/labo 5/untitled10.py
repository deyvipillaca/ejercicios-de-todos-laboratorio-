def palabras_con_letra(conjunto_palabras, letra):
    palabras_filtradas = set()
    for palabra in conjunto_palabras:
        if letra in palabra:
            palabras_filtradas.add(palabra)
    return palabras_filtradas

# Ejemplo de uso
palabras = {"casa", "perro", "gato", "oso", "elefante"}
letra_deseada = "o"
palabras_con_letra_deseada = palabras_con_letra(palabras, letra_deseada)

print(f"Palabras que contienen la letra '{letra_deseada}':", palabras_con_letra_deseada)
