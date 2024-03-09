class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

# Crear una lista enlazada de ejemplo
lista = ListaEnlazada()
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Calcular la suma de todos los nodos en la lista enlazada
suma_total = lista.sumar_nodos()

print("La suma de todos los nodos en la lista enlazada es:", suma_total)
