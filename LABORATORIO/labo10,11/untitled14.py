class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

# Inicializar las pilas para números y deshaceres
pila_numeros = Pila()
pila_deshaceres = Pila()

def realizar_operacion(operacion):
    pila_numeros.apilar(operacion)
    # Realizar la operación (aquí se simula la operación)

def deshacer_operacion():
    operacion_deshacer = pila_numeros.desapilar()
    if operacion_deshacer:
        pila_deshaceres.apilar(operacion_deshacer)
        # Deshacer la operación (aquí se simula el deshacer)

def rehacer_operacion():
    operacion_rehacer = pila_deshaceres.desapilar()
    if operacion_rehacer:
        pila_numeros.apilar(operacion_rehacer)
        # Rehacer la operación (aquí se simula el rehacer)

# Ejemplo de uso del sistema "deshacer" con números
realizar_operacion(5)
realizar_operacion(10)
print("Números ingresados:", pila_numeros.items)

deshacer_operacion()
print("Números después de deshacer:", pila_numeros.items)
print("Números deshechos:", pila_deshaceres.items)

rehacer_operacion()
print("Números después de rehacer:", pila_numeros.items)
print("Números deshechos después de rehacer:", pila_deshaceres.items)
