'''
Crea un algoritmo que genere los datos de "reading_score" y "math_score" en variables categóricas
 (puedes utilizar el criterio de pasar o reprobar una materia, por ejemplo, 
 un valor arriba de 70 significa aprobatorio mientras que uno menor equivale a no aprobatorio), 
 y guárdalo en dos columnas diferentes (cada columna nueva representa la nueva columna con variables categórica).
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

alumnos = pd.read_csv("ACTIVIDAD20/cleanstudentscomplete-2.csv")

alumnos = alumnos[["reading_score", "math_score"]]

reading_score =alumnos[["reading_score"]]

valores = {-math.inf,70,math.inf}
categorias = ["no aprobado", "aprobado"]
alumnos['cat_read']= pd.cut(x=alumnos['reading_score'], bins =valores, labels=categorias)
print( alumnos)