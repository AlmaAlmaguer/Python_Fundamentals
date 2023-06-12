'''Cada compañero dirá un número. Los guardarás en un diccionario, junto con el nombre del compañero.
imprimir los valores del diccionario (nombre de la persona y número que dijo) (Usando un bucle for)
imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número.
'''
jugadores=0
persona = 'S'
diccionario = {}
while (persona =='S'):
    nombre = input("Ingrese su nombre: ")
    numero = int(input('Ingrese un numero: '))
    diccionario [nombre] = numero
    persona = input("Ingresar nuevo socio S para continuar: ")


mayor = 0
menor = numero
for nombre, numero  in diccionario.items():
   print(nombre,numero)
   if (mayor< numero):
       mayor = numero
   if(menor>numero ):
       menor=numero
print('\n')
print('El numero Mayor es:', mayor)
print('El numero Menor es:', menor)
    
    







'''
jugadores+=1
diccionario [i][jugadores]=  numero
for
'''
