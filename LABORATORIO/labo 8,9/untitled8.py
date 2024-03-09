# Definir una variable inicial
variable = 5

# Realizar una operación que modifica el valor de la variable
variable *= 2  # Multiplicar por 2

# Validar el estado de la variable después de la operación
valor_esperado = 10
assert variable == valor_esperado, f"La variable debería ser {valor_esperado}, pero es {variable}"
print("El estado de la variable después de la operación es el esperado.")
