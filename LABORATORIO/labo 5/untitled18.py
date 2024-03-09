def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    palabras_filtradas = {palabra for palabra in conjunto_palabras if letra in palabra}
    palabras_filtradas_ordenadas = sorted(palabras_filtradas, reverse=True)
    return palabras_filtradas_ordenadas

# Ejemplo de uso
palabras = {"casa", "perro", "gato", "oso", "elefante"}
letra_deseada = "o"
palabras_con_letra_ordenadas = palabras_con_letra_ordenadas(palabras, letra_deseada)

print(f"Palabras que contienen la letra '{letra_deseada}' ordenadas de mayor a menor:", palabras_con_letra_ordenadas)
