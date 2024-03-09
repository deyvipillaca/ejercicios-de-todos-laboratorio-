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

def ordenar_pila_ascendente(pila):
    lista_temporal = []
    pila_ordenada = Pila()

    # Mover elementos de la pila a una lista para ordenarlos
    while not pila.esta_vacia():
        lista_temporal.append(pila.desapilar())

    # Ordenar la lista temporal
    lista_temporal.sort()

    # Mover elementos ordenados de la lista a la pila ordenada
    for elemento in lista_temporal:
        pila_ordenada.apilar(elemento)

    return pila_ordenada

# Crear una pila con elementos desordenados
pila_original = Pila()
pila_original.apilar(5)
pila_original.apilar(2)
pila_original.apilar(8)
pila_original.apilar(1)
pila_original.apilar(3)

# Ordenar los elementos de la pila de manera ascendente
pila_ordenada = ordenar_pila_ascendente(pila_original)

# Imprimir los elementos ordenados de la pila
print("Elementos ordenados de la pila de manera ascendente:")
while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar())
