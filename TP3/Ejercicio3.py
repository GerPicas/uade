#Desarrollar un programa que solicite un número de mes (por ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y mostrar un mensaje de error en caso de que no lo sea.

numMes = int(input("Ingrese el numero de algun mes: "))

uno = "enero"
dos = "febrero"
tres = "marzo"
cuatro = "abril"
cinco = "mayo"
seis = "junio"
siete = "julio"
ocho = "agosto"
nueve = "septiembre"
diez = "octubre"
once = "noviembre"
doce = "diciembre"

if numMes == 1: 
    print("El mes es", uno)
elif numMes == 2: 
    print("El mes es", dos) 
elif numMes == 3: 
    print("El mes es", tres)
elif numMes == 4: 
    print("El mes es", cuatro)
elif numMes == 5: 
    print("El mes es", cinco)
elif numMes == 6: 
    print("El mes es", seis)
elif numMes == 7: 
    print("El mes es", siete)
elif numMes == 8: 
    print("El mes es", ocho)
elif numMes == 9: 
    print("El mes es", nueve)
elif numMes == 10: 
    print("El mes es", diez)
elif numMes == 11: 
    print("El mes es", once)
elif numMes == 12: 
    print("El mes es", doce)
else: 
    print("Ingreso un numero invalido")
