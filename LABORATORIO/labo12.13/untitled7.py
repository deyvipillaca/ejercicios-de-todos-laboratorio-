class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_internos(arbol):
    if arbol is None or (arbol.izquierda is None and arbol.derecha is None):
        return 0
    return 1 + contar_nodos_internos(arbol.izquierda) + contar_nodos_internos(arbol.derecha)

# Ejemplo de uso
# Construir un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)

# Calcular la cantidad de nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print("La cantidad de nodos internos en el árbol es:", cantidad_nodos_internos)

