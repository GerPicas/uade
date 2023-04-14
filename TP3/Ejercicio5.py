#Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico del libro es de $500, más $3,20 por página con encua-dernación rústica. Si el número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo en $200. Además, si el número de páginas sobrepasa las 600 se hace necesario un procedimiento especial de en-cuadernación que incrementa el costo en otros $336. Desarrollar un programa que calcule el costo de un libro dado el número de páginas.

#libro < 300: 500pe encuadernacion rustica/ 3,20$ por pagina/ libro > 500 paginas: 300pe + 200pe/ libro > 600 paginas: 300 + 200 + 336


libro= int(input("Ingrese las paginas que tiene el libro: "))

encuadernacionRustica = (libro * 3.20) + 500
encuadernacionTela = (libro * 3.20) + 500 + 200
encuadernacionEspecial = (libro * 3.20) +500 + 200 + 336

if libro > 0 and libro <= 300: 
    print("El coste del libro es: $", encuadernacionRustica)
elif libro > 300 and libro < 600:
    print("El coste del libro es: $", encuadernacionTela)
elif libro >= 600:
    print("El coste del libro es: $", encuadernacionEspecial)