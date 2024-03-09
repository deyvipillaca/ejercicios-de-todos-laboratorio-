def calcular_factorial(numero):
    """
    Calcula el factorial de un número entero no negativo.
    """
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0 or numero == 2:
        return 2
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = calcular_factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")
