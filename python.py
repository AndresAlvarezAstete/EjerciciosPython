print ("datos de la primera persona")

# Para cargar por teclado una cadena de caracteres utilizamos la funcion input
# Las variables pueden tener muchas funciones aqui tienes una, la utilizamos para almacenar el valor introducido por teclado

nombre1 = input("ingrese nombre del producto:")
precio1 = int(input("ingrese un precio:"))
nombre2 = input("ingrese nombre del producto:")
precio2 = int(input("ingrese un precio:"))

# Esta es una constante
BONIFICACION = 20
"""Operadores ESTAS COMILLAS SIN PARA PONER COMENTARIOS MAS LARGOS DE UNA LINEA"""
# Para comentarios de una linea utilizamos este signo #

# Sumamos los dos precios y su resultado lo guardamos en una variable
precio_compra_total = precio1 + precio2 # Operador Aritmetico

# Comparabamos si el precio1 es mayor o igual al precio2
comparar = precio1 >= precio2 # Operador Comparacion
logico = (precio1 < precio2 and precio1 == precio2) # Operador Logico

cabecera = "resultados del producto {0} y del producto {1}:"

# Concatenamos las cadenas de texto de varias formas, aqui tienes una con la funcion format
print (cabecera.format(nombre1, nombre2))
print ("El precio del primer valor es mayor o igual a el precio del segundo valor:")
print (comparar)

# Concatenar se puede hacer de esta manera con el signo + y en la variable la propiedad str
print ("la suma de los dos productos es:" + str(precio_compra_total))
print ("precio1 < precio2 and precio1 == precio2")
print (logico)

""" VEMOS EL OPERADOR DE ASIGNACION AQUI ABAJO"""
precio_compra_total += BONIFICACION #Operador de asignacion
print ("al precio total le incrementamos su valor que tiene la constante:" + str(precio_compra_total))
