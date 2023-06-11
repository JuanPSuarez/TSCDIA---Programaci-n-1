mayores = 0
menores = 0
maximo = float('-inf')
minimo = float('inf')

for i in range(10):
    numero = int(input("Ingrese un número: "))
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
    if numero > 100:
        mayores += 1
    if numero < 100:
        menores += 1

print("Cantidad de números mayores a 100:", mayores)
print("Cantidad de números menores a 100:", menores)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)
