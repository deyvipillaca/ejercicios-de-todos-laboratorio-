# Generar los primeros 10 números de la serie Fibonacci usando una función recursiva
def fibonacci_recursivo(n):
    if n <= 2:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

fibonacci = [fibonacci_recursivo(i) for i in range(10)]

print("Los primeros 10 números de la serie Fibonacci son:")
print(fibonacci)

