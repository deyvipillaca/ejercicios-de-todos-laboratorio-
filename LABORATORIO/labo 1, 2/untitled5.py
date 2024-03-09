def es_primo(numero):
    """
    Verifica si un número es primo.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**4) + 1):
        if numero % i == 0:
            return False
    return True

# Ingreso de un número por el usuario
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

# Verificación y resultado
if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")

