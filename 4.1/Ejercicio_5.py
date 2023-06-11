opcion = input("Seleccione la conversión:\n1. Pesos a dólares\n2. Dólares a pesos\nIngrese el número de opción: ")

if opcion == "1":
    pesos = float(input("Ingrese la cantidad en pesos: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    dolares = pesos / tipo_cambio
    print(f"{pesos} pesos equivale a {dolares} dólares.")
elif opcion == "2":
    dolares = float(input("Ingrese la cantidad en dólares: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    pesos = dolares * tipo_cambio
    print(f"{dolares} dólares equivale a {pesos} pesos.")
else:
    print("Opción no válida. Ingrese '1' o '2'.")
