inversion = float(input("Ingrese dinero invertido: "))
meses = int(input("Ingrese la cantidad de meses que piensa invertir: "))

retornoTiempo = 2 * meses
retornoInversion = ((retornoTiempo * inversion) / 100) + inversion


print("Ganara: $",retornoInversion)