import numpy as np 
'''
1.- Crear una matriz 3x3 con valores de 0 a 8
2.- Crear una matriz identidad de 6x6 utilizando la función .identity().
'''

'''PASO 1 Crear una matriz 3x3 con valores de 0 a 8'''
matriz= np.reshape(np.array(range(0,9)),(3,3))

print(matriz )
print ('\n')

'''PASO 2 Crear una matriz identidad de 6x6 utilizando la función .identity()'''
midentidad = np.identity(6)
print(midentidad)

