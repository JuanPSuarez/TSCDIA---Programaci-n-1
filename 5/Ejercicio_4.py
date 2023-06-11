sumatoria_positivos = 0

for i in range(10):
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        print(numero)
        sumatoria_positivos += numero

print("Sumatoria de los números positivos:", sumatoria_positivos)
