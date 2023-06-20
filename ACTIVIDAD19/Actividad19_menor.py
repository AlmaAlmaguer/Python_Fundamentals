'''
Crea una gráfica que describa cuántos alumnos por escuela tuvieron el peor puntaje en "reading" 
(peor 10% de los puntajes), y con ello saber qué género es el que predomina en este filtro. 
Es importante imprimir el resultado de cuál es el género que mejor puntaje obtuvo para 
facilitar la interpretación de los resultados para el usuario.
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

school_labels=[]
school_men=[]
school_wom=[]

alumnos = pd.read_csv("ACTIVIDAD18/cleanstudentscomplete-1-1.csv")
alumnos = alumnos[["school_name","reading_score", "gender"]]

escuelas = alumnos['school_name'].unique()

for escuela in escuelas:
    escu = alumnos[alumnos['school_name'] == escuela]
    min_reading = escu['reading_score'].min()
    score_type= escu['reading_score'].unique()
    score_qty = score_type.size
    perc = score_qty *.10
    perc = round(perc)
    sorted_scores = np.sort(score_type)
    puntaje_reading = escu[escu['reading_score'] < sorted_scores[perc]]
    gender_type = puntaje_reading['gender'].unique()
    gender_qty = puntaje_reading['gender'].value_counts().tolist()
    formato_esc = escuela.replace(' ', '\n')
    school_labels.append(formato_esc)
    school_men.append(gender_qty[0])
    school_wom.append(gender_qty[1])

x = np.arange(len(school_labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, school_men, width, label='Men')
rects2 = ax.bar(x + width/2, school_wom, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(school_labels)
ax.legend()


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
autolabel(rects2)

fig.tight_layout()

plt.show()
plt.savefig("ACTIVIDAD19/Grafic_reading.png")

