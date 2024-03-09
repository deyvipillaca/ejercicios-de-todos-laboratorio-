def suma_numeros_pares(inicio, fin):
    """
    Calcula la suma de los números pares en un rango.
    """
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

# Ingreso del rango por el usuario
inicio_rango = int(input("Ingrese el inicio del rango: "))
fin_rango = int(input("Ingrese el final del rango: "))

# Cálculo y resultado
resultado_suma = suma_numeros_pares(inicio_rango, fin_rango)
print(f"La suma de los números pares en el rango de {inicio_rango} a {fin_rango} es: {resultado_suma}")

