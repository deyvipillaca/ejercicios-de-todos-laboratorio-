# Ingreso del número por el usuario
numero_ingresado = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero_ingresado}:")

for i in range(2, 13):
    resultado = numero_ingresado * i
    print(f"{numero_ingresado} x {i} = {resultado}")
