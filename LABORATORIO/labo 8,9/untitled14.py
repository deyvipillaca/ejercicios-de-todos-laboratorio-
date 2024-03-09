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

    def eliminar_duplicados(self):
        valores_unicos = set()
        actual = self.cabeza
        previo = None

        while actual:
            if actual.valor in valores_unicos:
                previo.siguiente = actual.siguiente
            else:
                valores_unicos.add(actual.valor)
                previo = actual
            actual = actual.siguiente

    def imprimir_lista(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual.valor)
            actual = actual.siguiente
        print("Lista Enlazada:", nodos)

# Crear una lista enlazada de ejemplo con nodos duplicados
lista = ListaEnlazada()
lista.agregar_nodo(10)
lista.agregar_nodo(20)
lista.agregar_nodo(10)
lista.agregar_nodo(30)
lista.agregar_nodo(20)

# Eliminar los nodos duplicados de la lista enlazada
lista.eliminar_duplicados()

# Imprimir la lista sin nodos duplicados
lista.imprimir_lista()
