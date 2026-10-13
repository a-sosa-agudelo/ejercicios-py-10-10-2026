import datetime

# 1. Uso de input() para solicitar el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Obtener la fecha actual usando el módulo datetime
fecha_actual = datetime.date.today()

# 2. Uso de print() para mostrar el mensaje de bienvenida y la fecha
print(f"¡Hola, {nombre}! Bienvenido a tu primer programa en Python.")
print(f"La fecha de ejecución de este programa es: {fecha_actual}")