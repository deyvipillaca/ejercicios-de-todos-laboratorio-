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

def eliminar_duplicados_pila(pila):
    pila_sin_duplicados = Pila()
    elementos_unicos = set()

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_unicos:
            pila_sin_duplicados.apilar(elemento)
            elementos_unicos.add(elemento)

    return pila_sin_duplicados

# Crear una pila con elementos duplicados
pila_original = Pila()
pila_original.apilar(5)
pila_original.apilar(2)
pila_original.apilar(5)
pila_original.apilar(8)
pila_original.apilar(2)

# Eliminar los elementos duplicados de la pila
pila_sin_duplicados = eliminar_duplicados_pila(pila_original)

# Imprimir los elementos únicos de la pila
print("Elementos únicos de la pila sin duplicados:")
while not pila_sin_duplicados.esta_vacia():
    print(pila_sin_duplicados.desapilar())
