class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def buscar_nodo(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return actual
            actual = actual.siguiente
        return None

# Crear una lista enlazada de ejemplo
lista = ListaEnlazada()
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Buscar un nodo con valor 20 en la lista enlazada
valor_buscado = 20
nodo_encontrado = lista.buscar_nodo(valor_buscado)

if nodo_encontrado:
    print(f"Se encontró un nodo con el valor {valor_buscado}.")
else:
    print(f"No se encontró un nodo con el valor {valor_buscado}.")


