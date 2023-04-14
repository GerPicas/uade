#Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está entre 0 y 10.∑Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.∑Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.∑Se debe recuperar cuando al menos una de las dos notas es menor a 4.

num1 = float(input("Ingrese la nota del primer parcial: "))
num2 = float(input("Ingrese la nota del segundo parcial: "))

if (num1 >= 7 and num1 <= 10) and (num2 >=7 and num2 <= 10):
    print("Promociono")
elif (num1 >= 4 or num1 >= 4) and (num1 <= 10 and num2 <= 10): 
    print("Aprobo")
elif (num1 < 4 or num2 < 4) and (num1 >= 4 or num2 >= 4):
    print("Debe recuperar")
elif num1 > 10 or num2 > 10: 
    print("No se han ingresado notas validas")

