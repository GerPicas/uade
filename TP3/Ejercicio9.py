#Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad. También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social: 3%, Sindicato: 3%. Como datos de entrada se ingresa por teclado el sueldo básico, antigüe-dad y estado civil (1 si es soltero o 2 si es casado)

sueldo = float(input("Ingrese su sueldo basico: "))
antiguedad = int(input("Ingrese la cantidad de años de antiguedad que tiene: "))
estadoCivil = int(input("Ingrese un 1 si es soltero o un 2 si es casado: "))

#Por cada año de antiguedad
soltero = sueldo * 0.05
casado = sueldo * 0.07
jubilacion = sueldo * 0.11
obraSocial = sueldo * 0.03
sindicato = sueldo * 0.03

sueldoTotalSoltero = sueldo + (soltero * antiguedad) - jubilacion - obraSocial - sindicato
sueldoTotalCasado = sueldo + (casado * antiguedad) - jubilacion - obraSocial - sindicato

if estadoCivil == 1: 
    print("Su sueldo es de: $", sueldoTotalSoltero)
elif estadoCivil == 2:
    print("Su sueldo es de: $", sueldoTotalCasado)
elif estadoCivil <= 0 or estadoCivil >= 3:
    print("Ingreso un numero erroneo")