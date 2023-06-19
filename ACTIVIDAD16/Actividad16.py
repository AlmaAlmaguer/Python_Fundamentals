'''
Crea una gráfica de barras que represente a los 10 países con más medallas ganadas. 
Se debe de ver claramente qué país pertenece a cada una de las barras representadas en el gráfico
'''
import matplotlib.pyplot as plt
import pandas as pd

atletas = pd.read_csv("ACTIVIDAD16/athlete_events-1.csv")
df = atletas
print(df.head(10))
paises_gan = df[["Team","Medal"]]
paises_gan = paises_gan[paises_gan["Medal"].notna()]

print(paises_gan)


x = paises_gan['Team'].unique()
y= paises_gan['Team'].value_counts().tolist()

diccionario= pd.DataFrame(dict(
    Team= x,
    Medal =y
))
ordenado = diccionario.sort_values("Medal", ascending=False)
final = ordenado[:10]
plt.rcParams['figure.figsize'] = [23,8]
plt.bar('Team', 'Medal', data=final)
plt.show()


