ventas = int(input("ingrese el numero de ventas que realizo el vendedor: "))
valorVentas = float(input("ingrese el total del valor de las propiedades vendidas por el empleado: "))
comision = valorVentas * 0.052

ganado = 50000 + (ventas * 5000) + comision

print("El vendedor ha gando : ",ganado)