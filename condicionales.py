# Utilizamos funcion input para introducir valores por teclado
sueldo = int(input("introduce el sueldo:"))

# Condicional if
if sueldo > 3000:
    print("El usuario debe pagar un porcentaje en impuestos")
if sueldo <= 3000: # Operador de comparacion
    print("El usuario esta exento de declarar renta")

if sueldo > 6000 and sueldo < 10000: # Operador logico se tiene que cumplir las dos condiciones
    print("El usuario tiene que pagar una bonificacion de 1000 euros")

if sueldo == 20000 or sueldo == 30000: # Operador logico solo se tiene que cumplir una de las dos condiciones
    print("El usuario paga un 10 por ciento de su sueldo")    