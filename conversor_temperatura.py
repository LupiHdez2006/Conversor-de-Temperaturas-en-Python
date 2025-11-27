def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

def fahrenheit_a_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_a_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def menu():
    while True:
        print("\n===== CONVERSOR DE TEMPERATURAS =====")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Celsius a Kelvin")
        print("4. Kelvin a Celsius")
        print("5. Fahrenheit a Kelvin")
        print("6. Kelvin a Fahrenheit")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        try:
            opcion = int(opcion)
        except ValueError:
            print("⚠ Por favor ingrese un número válido.")
            continue

        if opcion == 7:
            print("¡Gracias por usar el conversor!")
            break

        if opcion < 1 or opcion > 7:
            print("⚠ Opción fuera de rango.")
            continue

        try:
            valor = float(input("Ingrese la temperatura a convertir: "))
        except ValueError:
            print("⚠ Entrada inválida. Use solo números.")
            continue

        if opcion == 1:
            resultado = celsius_a_fahrenheit(valor)
            print(f"{valor} °C = {resultado:.2f} °F")

        elif opcion == 2:
            resultado = fahrenheit_a_celsius(valor)
            print(f"{valor} °F = {resultado:.2f} °C")

        elif opcion == 3:
            resultado = celsius_a_kelvin(valor)
            print(f"{valor} °C = {resultado:.2f} K")

        elif opcion == 4:
            resultado = kelvin_a_celsius(valor)
            print(f"{valor} K = {resultado:.2f} °C")

        elif opcion == 5:
            resultado = fahrenheit_a_kelvin(valor)
            print(f"{valor} °F = {resultado:.2f} K")

        elif opcion == 6:
            resultado = kelvin_a_fahrenheit(valor)
            print(f"{valor} K = {resultado:.2f} °F")


# Ejecutar el menú
menu()
