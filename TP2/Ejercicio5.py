nombre1 = input("Ingrese el nombre del primer inversor: ")
persona1 = float(input("Ingrese cuanto dinero invirtio: "))

nombre2 = input("Ingrese el nombre del segundo inversor: ")
persona2 = float(input("Ingrese cuanto dinero invirtio: "))

nombre3 = input("Ingrese el nombre del tercer inversor: ")
persona3 = float(input("Ingrese cuanto dinero invirtio: "))

total = persona1 + persona2 + persona3

porcentaje1 = (persona1 * 100) / total
porcentaje2 = (persona2 * 100) / total
porcentaje3 = (persona3 * 100) / total

print(nombre1, "invirtio", porcentaje1,"%")
print(nombre2, "invirtio", porcentaje2,"%")
print(nombre3, "invirtio", porcentaje3,"%")