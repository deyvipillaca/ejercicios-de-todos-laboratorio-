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

def verificar_anidacion_operadores(expresion):
    pila = Pila()
    parentesis = {'(': ')', '[': ']', '{': '}'}

    for caracter in expresion:
        if caracter in parentesis.keys():
            pila.apilar(caracter)
        elif caracter in parentesis.values():
            if pila.esta_vacia() or parentesis[pila.desapilar()] != caracter:
                return False

    return pila.esta_vacia()

# Expresión matemática a verificar
expresion = "((3 + 4) * 2)"

# Verificar anidación de operadores utilizando una pila
resultado_verificacion = verificar_anidacion_operadores(expresion)

if resultado_verificacion:
    print(f"Los operadores en la expresión '{expresion}' están correctamente anidados.")
else:
    print(f"Los operadores en la expresión '{expresion}' no están correctamente anidados.")
