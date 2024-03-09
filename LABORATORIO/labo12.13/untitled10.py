class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrar_minimo(raiz):
    if raiz is None:
        return None
    if raiz.izquierda is None:
        return raiz.valor
    return encontrar_minimo(raiz.izquierda)

# Ejemplo de uso
# Construir un árbol de ejemplo
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)

# Encontrar el nodo con el valor mínimo en el árbol
valor_minimo = encontrar_minimo(raiz)
print("El valor mínimo en el árbol es:", valor_minimo)
