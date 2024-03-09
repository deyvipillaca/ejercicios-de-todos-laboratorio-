def funcion_ejemplo():
    return 42  # Valor específico que se espera que retorne la función

# Llamar a la función y verificar si retorna el valor esperado
resultado = funcion_ejemplo()
valor_esperado = 42

assert resultado == valor_esperado, f"La función debería retornar {valor_esperado}, pero retornó {resultado}"
print("La función retornó el valor esperado.")
