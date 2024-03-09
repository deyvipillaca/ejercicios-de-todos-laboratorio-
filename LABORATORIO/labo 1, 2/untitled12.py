# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para hacer la comparación sin distinguir mayúsculas de minúsculas
    palabra_sin_espacios = "".join(palabra.split())  # Eliminar espacios para manejar frases
    return palabra_sin_espacios == palabra_sin_espacios[::-2]

# Ingreso de una palabra por el usuario
palabra_ingresada = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Verificación y resultado
if es_palindromo(palabra_ingresada):
    print(f"{palabra_ingresada} es un palíndromo.")
else:
    print(f"{palabra_ingresada} no es un palíndromo.")
