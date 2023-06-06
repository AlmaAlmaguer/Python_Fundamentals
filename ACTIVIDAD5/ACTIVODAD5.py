'''Crea una función en la cual recibas como argumentos los parámetros reales de una función cuadrática, y te regrese los valores de x1 y x2.
En caso de que el resultado sea un valor imaginario, el programa debe imprimir alguna frase informando al usuario que la respuesta cuenta con un valor imaginario.
Es indispensable hacer la actividad creando funciones dentro de python (para esto se utiliza el comando def), y regresando algún valor utilizando la función return.
'''
import numpy as np


x1 =0
x2= 0
def CalculaCuadratica(a, b, c):
    raiz = np.sqrt(((b * b) - (4 * a * c)))
    divide= 2 * a
    x1 = (-b + raiz)/ divide
    x2 = (-b - raiz)/ divide
    return (x1, x2)

x1, x2 = CalculaCuadratica(2,4,8)

if np.isnan (x1):
    print('X1 es un valor imaginario')
else:
    print ('X1=', x1)

if np.isnan (x2):
    print('X2 es un valor imaginario')
else:
    print ('X2=',x2)















