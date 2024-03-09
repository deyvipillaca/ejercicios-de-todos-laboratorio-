def imprimir_piramide(n, nivel=1):
    if nivel <= n:
        # Imprimir espacios en blanco para alinear los números en la pirámide
        print(" " * (n - nivel), end="")

        # Imprimir números ascendentes hasta el nivel actual
        for i in range(1, nivel + 1):
            print(i, end=" ")

        # Imprimir números descendentes desde el nivel actual - 1 hasta 1
        for i in range(nivel - 1, 0, -1):
            print(i, end=" ")

        print()  # Salto de línea para pasar al siguiente nivel
        imprimir_piramide(n, nivel + 1)

# Llamar a la función para imprimir la pirámide de números del 1 al n
n = 5  # Puedes cambiar el valor de n según la altura de la pirámide deseada
imprimir_piramide(n)

