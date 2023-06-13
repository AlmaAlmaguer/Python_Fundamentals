import pandas as pd
import numpy as np 
import csv

'''
Crear un programa en Visual Studio que me permita saber cuál es: 
-el competidor más veterano que ha recibido medalla (oro, plata o bronce)
-el competidor más joven que ha recibido medalla de oro
-el competidor más ganador de la historia
crea un csv con toda su información 
'''
atletas = pd.read_csv("ACTIVIDAD13/athlete_events.csv")

ganador = atletas[atletas['Medal'].notna()]

oro = ganador[ganador['Medal']=='Gold']

min_edad =oro['Age'].min()
competi_min = oro[oro['Age']== min_edad]
#oro = atletas[atletas['Age'].min()]

print (competi_min)
competi_min.to_csv ('ACTIVIDAD13/medallista_menor.csv', header =True, index = True)
print ('\n')



max_edad =ganador['Age'].max()
competi_max =ganador[ganador['Age']== max_edad]

competi_max.to_csv('ACTIVIDAD13/medallista_mayor.csv', header =True, index = True)
                 
print (competi_max)

maxganador =ganador.groupby(['ID','Name','Sex','Team','NOC','Sport']).count()
maxMedal =maxganador['Medal'].max()
competi_maxMed = maxganador[maxganador['Medal']== maxMedal]
print (competi_maxMed)

competi_maxMed.to_csv('ACTIVIDAD13/maximo_medallista.csv',header =True, index = True)
