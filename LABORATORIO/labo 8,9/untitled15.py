class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def invertir_lista(self):
        previo = None
        actual = self.cabeza

        while actual:
            siguiente_temporal = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente_temporal

        self.cabeza = previo

    def imprimir_lista(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual.valor)
            actual = actual.siguiente
        print("Lista Enlazada:", nodos)

# Crear una lista enlazada de ejemplo
lista = ListaEnlazada()
lista.agregar_nodo(10)
lista.agregar_nodo(20)
lista.agregar_nodo(30)

# Invertir el orden de la lista enlazada
lista.invertir_lista()

# Imprimir la lista enlazada invertida
lista.imprimir_lista()
