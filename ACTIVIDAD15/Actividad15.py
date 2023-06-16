'''
Obtener la diferencia entre el salario más alto y el más bajo dentro de los datos.
Para esto, se debe encontrar el valor máximo y restarle el valor mínimo de los datos 
(la respuesta a esta operación se llama rango de los datos).
'''
import numpy
import pandas as pd

salarios={
    "Nombre":["Ringo","John","Paul","Geroge","Yoko"],
    "Edad":[45,34,42,38,47],
    "Salario":[12000,14000,13000,11000,10000],
    "Genero":["M","M","M","M","F"]
}


pago_split= salarios["Salario"]


rango = max(pago_split) - min(pago_split)



print('arreglo', pago_split)
print('min_salario:',min_salario)
print('max_salario:',max_salario)
print ('rango', rango)



