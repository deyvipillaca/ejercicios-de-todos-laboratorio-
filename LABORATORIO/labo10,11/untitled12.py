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

def calcular_expresion(expresion):
    pila = Pila()
    operadores = set(['+', '-', '*', '/'])

    for elemento in expresion.split():
        if elemento not in operadores:
            pila.apilar(float(elemento))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if elemento == '+':
                resultado = operando1 + operando2
            elif elemento == '-':
                resultado = operando1 - operando2
            elif elemento == '*':
                resultado = operando1 * operando2
            elif elemento == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)

    return pila.desapilar()

# Solicitar al usuario ingresar la expresión matemática
expresion_usuario = input("Ingrese la expresión matemática en notación posfija (por ejemplo, '3 4 + 2 *'): ")

# Calcular el resultado de la expresión utilizando la calculadora con pila
resultado_calculadora = calcular_expresion(expresion_usuario)

print(f"El resultado de la expresión '{expresion_usuario}' es: {resultado_calculadora}")
