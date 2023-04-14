#Una remisería requiere un programa que calcule el precio de un viaje a partir de la cantidad de kilómetros que desea recorrer el usuario. Para eso cuenta con la siguiente tarifa:∑Viaje mínimo $250. Sólo se cobra cuando el importe por kilómetro no alcanza este mínimo.∑Si recorre entre 0 y 10 km: $30 por km∑Si recorre 10 km o más: $20 por km

#viaje minimo: entre 0 y 10km: 250pe/ si recorre 10km o mas: 20pe por km

viaje = float(input("Ingrese la cantidad de km que recorrio: "))

viajeMinimo = viaje * 30

viajeLargo = viaje * 20

if (viaje > 0 and viaje < 10) and viajeMinimo <= 250: 
    print("El coste del viaje es de: $", 250)
elif (viaje > 0 and viaje < 10) and viajeMinimo >= 250:
    print("El coste del viaje es de: $", viajeMinimo)
elif viaje >= 10:
    print("El coste del viaje es de: $", viajeLargo)