from datetime import datetime

def validar_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    
    if edad >= 18:
        print("El usuario es mayor de edad.")
    else:
        print("El usuario es menor de edad.")

# Solicitar al usuario que ingrese su fecha de nacimiento en formato YYYY-MM-DD
fecha_str = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_str, "%Y-%m-%d")

# Validar la edad del usuario
validar_edad(fecha_nacimiento)
