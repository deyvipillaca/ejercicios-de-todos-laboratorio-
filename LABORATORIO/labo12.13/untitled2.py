class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

def agregar_pedido(pedido, cola_pedidos):
    cola_pedidos.encolar(pedido)
    print(f"Pedido '{pedido}' agregado a la cola.")

def procesar_pedido(cola_pedidos):
    if not cola_pedidos.esta_vacia():
        pedido = cola_pedidos.desencolar()
        print(f"Procesando pedido: '{pedido}'")
    else:
        print("No hay pedidos en espera.")

def mostrar_estado_cola(cola_pedidos):
    if not cola_pedidos.esta_vacia():
        print("Pedidos en espera:")
        for pedido in cola_pedidos.items:
            print(pedido)
    else:
        print("No hay pedidos en espera.")

# Inicializar la cola de pedidos
cola_pedidos = Cola()

# Ejemplo de uso del sistema de gestión de pedidos
agregar_pedido("Pizza", cola_pedidos)
agregar_pedido("Hamburguesa", cola_pedidos)
agregar_pedido("Ensalada", cola_pedidos)

mostrar_estado_cola(cola_pedidos)

procesar_pedido(cola_pedidos)
procesar_pedido(cola_pedidos)

mostrar_estado_cola(cola_pedidos)
