class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def calcular_altura(arbol):
    if arbol is None:
        return 0
    altura_izquierda = calcular_altura(arbol.izquierda)
    altura_derecha = calcular_altura(arbol.derecha)
    return 1 + max(altura_izquierda, altura_derecha)

# Ejemplo de uso
# Construir un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)

# Calcular la altura del árbol
altura_arbol = calcular_altura(raiz)
print("La altura del árbol es:", altura_arbol)
