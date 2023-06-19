
'''
Crear y guardar una gráfica de pay del año más reciente existente en la base de datos.
 Se debe de leer claramente los datos dentro del gráfico, 
 por lo que se debe de encontrar alguna manera de organizarlo para que el usuario pueda interpretar claramente la gráfica.
'''
import matplotlib.pyplot as plt
import pandas as pd

atletas = pd.read_csv("ACTIVIDAD17/athlete_events-2.csv")
atletas = atletas[["Year","Medal"]]

medal_anio = atletas
medal_anio = medal_anio[atletas["Medal"].notna()]

print(medal_anio)
max_anio=medal_anio['Year'].max()

medal_anio= medal_anio[ medal_anio['Year'] == max_anio]


x = medal_anio['Medal'].unique()
y= medal_anio['Medal'].value_counts().tolist()

plt.pie(y, labels=x, autopct='%1.1f%%')
plt.show()

plt.savefig("ACTIVIDAD17/Grafic.png")

