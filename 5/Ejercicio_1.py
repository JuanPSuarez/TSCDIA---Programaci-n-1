numeros = []
pares = 0
suma_pares = 0

for i in range(4):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
        suma_pares += numero

impares = 4 - pares

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Sumatoria de los números pares:", suma_pares)
