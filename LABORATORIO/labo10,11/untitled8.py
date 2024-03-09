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

def evaluar_expresion_posfija(expresion):
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

# Expresión matemática en notación posfija
expresion_posfija = "3 4 + 2 *"

# Evaluar la expresión posfija utilizando una pila
resultado_evaluacion = evaluar_expresion_posfija(expresion_posfija)

print(f"El resultado de la expresión posfija '{expresion_posfija}' es: {resultado_evaluacion}")

