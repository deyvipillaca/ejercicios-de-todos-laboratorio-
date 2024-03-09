class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos(arbol):
    if arbol is None:
        return 0
    return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha)

# Ejemplo de uso
# Construir un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

# Calcular la cantidad de nodos en el árbol
cantidad_nodos = contar_nodos(raiz)
print("La cantidad de nodos en el árbol es:", cantidad_nodos)
