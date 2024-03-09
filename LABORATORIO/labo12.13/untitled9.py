class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def calcular_profundidad(raiz, valor_nodo, profundidad_actual=0):
    if raiz is None:
        return -1
    if raiz.valor == valor_nodo:
        return profundidad_actual
    profundidad_izquierda = calcular_profundidad(raiz.izquierda, valor_nodo, profundidad_actual + 1)
    if profundidad_izquierda != -1:
        return profundidad_izquierda
    profundidad_derecha = calcular_profundidad(raiz.derecha, valor_nodo, profundidad_actual + 1)
    return profundidad_derecha

# Ejemplo de uso
# Construir un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)

# Calcular la profundidad de un nodo específico (por ejemplo, el nodo con valor 5)
valor_nodo = 5
profundidad_nodo = calcular_profundidad(raiz, valor_nodo)
if profundidad_nodo != -1:
    print(f"La profundidad del nodo con valor {valor_nodo} es: {profundidad_nodo}")
else:
    print(f"No se encontró el nodo con valor {valor_nodo} en el árbol.")
