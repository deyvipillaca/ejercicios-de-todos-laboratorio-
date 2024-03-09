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

    def concatenar_listas(self, otra_lista):
        if not self.cabeza:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza

    def imprimir_lista(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual.valor)
            actual = actual.siguiente
        print("Lista Enlazada:", nodos)

# Crear dos listas enlazadas de ejemplo
lista1 = ListaEnlazada()
lista1.agregar_nodo(10)
lista1.agregar_nodo(20)

lista2 = ListaEnlazada()
lista2.agregar_nodo(30)
lista2.agregar_nodo(40)

# Concatenar las dos listas enlazadas
lista1.concatenar_listas(lista2)

# Imprimir la lista concatenada
lista1.imprimir_lista()
