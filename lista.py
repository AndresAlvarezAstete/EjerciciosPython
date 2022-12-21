lista = [] # Declaramos la lista
for k in range(10):
    lista.append(input("Introduce valor en la lista:")) # Añadimos los valores de la lista por teclado

print("Los elementos de la lista son:" + str(lista)) # Visualizamos los elementos de la lista
valor = int(input("Introduce el valor a modificar de la lista por el indice:")) # Indice a modificar
nuevo = input("Introduce el nuevo valor:") # Valor nuevo de indice que se modificara
lista[valor] = nuevo # Hacemos la modificacion
print("Los elementos de la lista son:" + str(lista)) # Visualizamos los elementos para comprobar la modificacion
valor = int(input("Introduce el indice en el que se intertara el nuevo valor:")) # Indique donde se insertara el nuevo valor
nuevo = input("Introduce el nuevo valor:") # valor a insertar
lista.insert(valor, nuevo)
print("Los elementos de la lista son:" + str(lista)) # Visualizamos los elementos para comprobar la modificacion
nuevo = input("Introduce el valor a eliminar:") # Valor a eliminar
lista.remove(nuevo) # Eliminamos el valor
print("Los elementos de la lista son:" + str(lista)) # Visualizamos lista
nuevo = input("Introduce el valor a buscar:")
resultado = (nuevo in lista)
if (resultado):
    print("Existe este elemento y su indice es: " + str(lista.index(nuevo)))
else:
    print("No existe el elemento")