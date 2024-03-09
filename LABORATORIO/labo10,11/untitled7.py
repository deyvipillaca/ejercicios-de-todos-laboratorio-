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

def decimal_a_binario(decimal):
    pila = Pila()

    while decimal > 0:
        resto = decimal % 2
        pila.apilar(resto)
        decimal = decimal // 2

    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())

    return binario

# Número decimal a convertir a binario
numero_decimal = 27

# Convertir el número decimal a binario utilizando una pila
numero_binario = decimal_a_binario(numero_decimal)

print(f"Número decimal {numero_decimal} en binario es: {numero_binario}")
