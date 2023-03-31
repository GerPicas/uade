segundos = int(input("Ingrese cierta cantidad de segundos: "))

minutos = segundos / 60
horas = minutos / 60
dias = horas / 24
segundos = minutos * 60

print("Esos segundos son: ", dias,"dias,", horas,"horas,", minutos,"minutos y", segundos,"segundos")