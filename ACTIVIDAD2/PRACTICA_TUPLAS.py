'''
1.- Crea una tupla con una longitud de 5 usando diferentes tipos de datos.
2.- Cambiar dicha tupla a una lista.
3.- Crea un diccionario donde la clave sea del 1 al 5 y los elementos los datos de la lista.
Utilizar la función "list" para la elaboración de la actividad.
'''

tupla = (2,10.5,'hola',True,['i','a'])
print (type(tupla))

lista = list(tupla)
print (type(lista))

diccionario = {}
for i in range(5):
    diccionario[i+1] = lista[i]
print (diccionario)


