# Variable de control inicializada en True para garantizar al menos una ejecución
ejecutar_ciclo = True

while ejecutar_ciclo:
    # Código que se ejecutará al menos una vez
    print("Este código se ejecutará al menos una vez.")

    # Actualizar la variable de control según alguna condición
    ejecutar_ciclo = False  # En este caso, se establece en False para salir del ciclo después de la primera ejecución

