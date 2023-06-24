'''
Crea un algoritmo que genere los datos de "reading_score" y "math_score" en variables categóricas
 (puedes utilizar el criterio de pasar o reprobar una materia, por ejemplo, 
 un valor arriba de 70 significa aprobatorio mientras que uno menor equivale a no aprobatorio), 
 y guárdalo en dos columnas diferentes (cada columna nueva representa la nueva columna con variables categórica).

 Crea una gráfica que condense la información obtenida ahora categóricamente.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

school_labels=[]
aprobados_reading=[]
no_aprobados_reading=[]

aprobados_math=[]
no_aprobados_math=[]



reading_scores=[]
math_scores=[]

alumnos = pd.read_csv("ACTIVIDAD20/cleanstudentscomplete-2.csv")

#valores = {0,70,100}
valores = [0,69,101]
categorias = ["no aprobado", "aprobado"]

escuelas = alumnos['school_name'].unique()

for escuela in escuelas: 
    escu = alumnos[alumnos['school_name'] == escuela]
    escu['cat_read']= pd.cut(x=escu['reading_score'], bins =valores, labels=categorias)
    escu['cat_math']= pd.cut(x=escu['math_score'], bins =valores, labels=categorias)
    
    formato_ptj = escuela.replace(' ', '\n')
    school_labels.append(formato_ptj)
    
    reading_scores = escu['cat_read'].value_counts().tolist()
    aprobados_reading.append(reading_scores[0])
    no_aprobados_reading.append(reading_scores[1])

    math_scores = escu['cat_math'].value_counts().tolist()
    aprobados_math.append(math_scores[0])
    no_aprobados_math.append(math_scores[1])

x = np.arange(len(school_labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
aprove_Rea = ax.bar(x - width/2, aprobados_reading, width, label='Reading Aprove')
no_aprove_Rea = ax.bar(x - width/2, no_aprobados_reading, width, label='Reading No Aprove')
aprove_Math = ax.bar(x + width/2, aprobados_math, width, label='Math Aprove')
no_aprove_Math = ax.bar(x + width/2, no_aprobados_math, width, label='Math No Aprove')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Número de Alumnos')
ax.set_title('Materias Por Escuela')
ax.set_xticks(x)
ax.set_xticklabels(school_labels)
ax.legend()
ax.figsize = [30,8]

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(aprove_Rea)
autolabel (no_aprove_Rea)
autolabel(aprove_Math)
autolabel(no_aprove_Math)

fig.tight_layout()

plt.show()
plt.savefig("ACTIVIDAD19/Grafic_reading.png")



