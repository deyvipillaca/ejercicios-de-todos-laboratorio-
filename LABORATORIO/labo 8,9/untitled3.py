def validar_calificacion(calificacion):
    if calificacion >= 0 and calificacion <= 10:
        print("La calificación es válida.")
    else:
        print("La calificación está fuera del rango permitido (debe ser entre 0 y 10).")

# Solicitar al usuario que ingrese la calificación
calificacion = float(input("Ingresa la calificación: "))

# Validar el rango de la calificación
validar_calificacion(calificacion)


