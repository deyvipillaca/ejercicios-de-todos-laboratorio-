class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrar_maximo(raiz):
    if raiz is None:
        return None
    if raiz.derecha is None:
        return raiz.valor
    return encontrar_maximo(raiz.derecha)

# Ejemplo de uso
# Construir un árbol de ejemplo
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)

# Encontrar el nodo con el valor máximo en el árbol
valor_maximo = encontrar_maximo(raiz)
print("El valor máximo en el árbol es:", valor_maximo)
