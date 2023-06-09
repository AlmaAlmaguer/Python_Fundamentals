'''
Utilizando la actividad de Puntaje Reading anterior, 
identifica a los alumnos con el mismo apellido que van en la misma escuela 
y evalúa las familias (misma escuela, mismo apellido) que tengan mejor puntaje en "reading". 
Presenta tus resultados de forma visual e imprimiendo un pequeño análisis sobre los resultados obtenidos.
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

school_labels=[]
first_place=[]
second_place=[]

alumnos = pd.read_csv("ACTIVIDAD20/cleanstudentscomplete-2.csv")
escuelas = alumnos['school_name'].unique()

for escuela in escuelas:
    escu = alumnos[alumnos['school_name'] == escuela]
    max_reading = escu['reading_score'].max()
    score_type= escu['reading_score'].unique()
    score_qty = score_type.size
    perc = score_qty *.10
    perc = round(perc)
    sorted_scores = np.sort(score_type)[::-1]
    puntaje_reading = escu[escu['reading_score'] > sorted_scores[perc]]
    
    puntaje_reading['Last'] = (puntaje_reading['student_name'].str.split(expand=True))[1]
    Last_type = puntaje_reading['Last'].unique()
    Last_qty = puntaje_reading['Last'].value_counts().tolist()

    Last_1 = puntaje_reading[puntaje_reading['Last'] == Last_type[0]]
    max_reading_1 = Last_1['reading_score'].max()

    formato_esc = escuela.replace(' ', '\n')
    formato_esc = Last_type[0] + "\n" + formato_esc
    school_labels.append(formato_esc)
    first_place.append(max_reading_1)

x = np.arange(len(school_labels)) # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, first_place, width, label='1er')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
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
autolabel(rects1)

fig.tight_layout()
plt.show()
plt.savefig("ACTIVIDAD19/Grafic_reading.png")
