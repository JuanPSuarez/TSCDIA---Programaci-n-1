mujeres = 0
varones = 0
mayores_edad = 0
menores_edad = 0

for i in range(15):
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona (M/F): ")

    if sexo == "F":
        mujeres += 1
    elif sexo == "M":
        varones += 1

    if edad >= 18:
        mayores_edad += 1
    else:
        menores_edad += 1

print("Cantidad de mujeres:", mujeres)
print("Cantidad de varones:", varones)
print("Cantidad de personas mayores de edad:", mayores_edad)
print("Cantidad de personas menores de edad:", menores_edad)
