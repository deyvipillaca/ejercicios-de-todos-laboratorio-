class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def es_palindroma(palabra):
    cola = Cola()

    # Encolar los caracteres de la palabra en orden original
    for letra in palabra:
        cola.encolar(letra)

    palabra_inversa = ""
    
    # Desencolar los caracteres para construir la palabra en orden inverso
    while not cola.esta_vacia():
        palabra_inversa += cola.desencolar()

    # Comparar la palabra original con la inversa para determinar si es palíndroma
    return palabra == palabra_inversa

# Ejemplo de uso para verificar si una palabra es palíndroma
palabra = "reconocer"

if es_palindroma(palabra):
    print(f"La palabra '{palabra}' es palíndroma.")
else:
    print(f"La palabra '{palabra}' no es palíndroma.")

