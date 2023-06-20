'''
Crea una gráfica que describa cuántos alumnos hay por cada grado.
 La gráfica debe ser clara y fácil de interpretar para el usuario. 
'''
import matplotlib.pyplot as plt
import pandas as pd

def labels(x,y):

    for i in range(len(x)):
        plt.text(i,y[i]//2,y[i], ha='center')

alumnos = pd.read_csv("ACTIVIDAD18/cleanstudentscomplete-1-1.csv")
alumnos = alumnos[["grade"]]



x = alumnos['grade'].unique()
y= alumnos['grade'].value_counts().tolist()


diccionario= pd.DataFrame(dict(
    grade= x,
    cantidad =y
))
ordenado = diccionario.sort_values("cantidad", ascending=True)

plt.rcParams['figure.figsize'] = [23,8]
plt.bar('grade', 'cantidad', data=ordenado)
labels(ordenado['grade'].tolist(),ordenado['cantidad'].tolist())
plt.title("ALUMNOS POR GRADO")
plt.xlabel("GRADOS")
plt.ylabel("ALUMNOS")

plt.show()

plt.savefig("ACTIVIDAD18/Grafic_alumnos.png")
