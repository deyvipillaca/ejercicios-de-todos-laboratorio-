class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def longitud_lista(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

# Crear una lista enlazada de ejemplo
lista = ListaEnlazada()
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Obtener la longitud de la lista enlazada
longitud = lista.longitud_lista()

print("La longitud de la lista enlazada es:", longitud)
