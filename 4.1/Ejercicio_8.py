importe = float(input("Ingrese el importe a pagar: "))
forma_pago = int(input("Seleccione la forma de pago:\n1. Contado\n2. Tarjeta\n3. Débito\nIngrese el número de opción: "))

if forma_pago == 1:
    descuento = importe * 0.10
    importe_total = importe - descuento
    print(f"Importe: {importe}")
    print(f"Descuento: {descuento}")
    print(f"Importe total: {importe_total}")
elif forma_pago == 2:
    interes = importe * 0.10
    importe_total = importe + interes
    print(f"Importe: {importe}")
    print(f"Interés: {interes}")
    print(f"Importe total: {importe_total}")
elif forma_pago == 3:
    descuento = importe * 0.05
    importe_total = importe - descuento
    print(f"Importe: {importe}")
    print(f"Descuento: {descuento}")
    print(f"Importe total: {importe_total}")
else:
    print("Forma de pago no válida. Ingrese '1', '2' o '3'.")
