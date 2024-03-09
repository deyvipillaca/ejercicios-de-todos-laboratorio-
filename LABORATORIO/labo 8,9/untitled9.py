try:
    import math
    modulo_importado = True
except ImportError:
    modulo_importado = False

# Verificar si el módulo se ha importado correctamente
assert modulo_importado, "Error: No se pudo importar el módulo 'math'."
print("El módulo 'math' se ha importado correctamente.")
