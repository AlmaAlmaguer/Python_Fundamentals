'''
Utilizar la función "list" para la elaboración de la actividad.
'''

'''ACTIVIDAD 1 Crea una tupla con una longitud de 5 usando diferentes tipos de datos.'''

tupla = (2,10.5,'hola',True,['i','a'])
print (type(tupla))

'''ACTIVIDAD 2 Cambiar dicha tupla a una lista.'''

lista = list(tupla)
print (type(lista))


'''ACTIVIDAD 3 rea un diccionario donde la clave sea del 1 al 5 y los elementos los datos de la lista.'''

diccionario = {}
for i in range(5):
    diccionario[i+1] = lista[i]
print (diccionario)


