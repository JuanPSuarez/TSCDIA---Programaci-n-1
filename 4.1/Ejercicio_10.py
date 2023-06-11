numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    dia_semana = "Lunes"
elif numero == 2:
    dia_semana = "Martes"
elif numero == 3:
    dia_semana = "Miércoles"
elif numero == 4:
    dia_semana = "Jueves"
elif numero == 5:
    dia_semana = "Viernes"
elif numero == 6:
    dia_semana = "Sábado"
elif numero == 7:
    dia_semana = "Domingo"
else:
    dia_semana = "Número inválido"

print("El día de la semana correspondiente es:", dia_semana)
