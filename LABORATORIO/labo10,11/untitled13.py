class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def es_palindromo(palabra):
    # Eliminar espacios y convertir a minúsculas para simplificar la comparación
    palabra = palabra.replace(" ", "").lower()
    
    pila = Pila()

    # Apilar los caracteres de la palabra en la pila
    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    
    # Desapilar los caracteres para construir la palabra invertida
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()

    # Comparar la palabra original con la invertida para determinar si es un palíndromo
    return palabra == palabra_invertida

# Solicitar al usuario ingresar la palabra o frase a verificar
palabra_usuario = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")

# Verificar si la palabra o frase es un palíndromo utilizando una pila
if es_palindromo(palabra_usuario):
    print(f"La palabra o frase '{palabra_usuario}' es un palíndromo.")
else:
    print(f"La palabra o frase '{palabra_usuario}' no es un palíndromo.")
