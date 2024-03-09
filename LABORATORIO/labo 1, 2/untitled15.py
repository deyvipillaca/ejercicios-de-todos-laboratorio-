# Ingreso del número entero por el usuario
numero = int(input(" número entero: "))

# Convertir el número a una cadena para iterar sobre sus dígitos
numero_str = str(abs(numero))  # Usamos abs() para manejar números negativos

# Calcular la suma de los dígitos
suma_digitos = sum(int(digito) for digito in numero_str)

# Mostrar el resultado
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
