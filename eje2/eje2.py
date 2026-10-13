print("--- CALCULADORA BÁSICA ---")

# 1. Entrada de datos (usamos float para permitir números con decimales)
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# 2. Menú de opciones
print("\nSelecciona una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1-4): ")

# 3. Operaciones matemáticas y salida por pantalla
if opcion == "1":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == "4":
    # Validación para evitar errores matemáticos
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor, ejecuta el programa nuevamente.")