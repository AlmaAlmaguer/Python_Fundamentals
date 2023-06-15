'''
Nombre: Alma Yesenia Almaguer
Empleado:3508931
Correo:alma.almaguer@oxxo.com 
Capacitación : 9 am -15 junio -2023
'''


import numpy 

def Validar(rango):
    caracter= rango.isdigit()
    if(caracter == False):
        return (False)
    elif (int(rango)<=0):
        return (False)
    else:
        return (True)

rango = input("Ingrese el rango que desea validar: ")

while(Validar(rango) == False):
    print('Ingrese un valor numerico mayor a 0')
    rango = input("Ingrese el rango que desea validar: ")


vector = list(range(1,int(rango)))

for i in range(int(rango)-1):
    if( vector[i] %3==0 and vector[i] %5==0):
        print('Fizzbuzz')
    elif(vector[i] %3==0):
        print('fizz')
    elif (vector[i] %5 == 0):
        print('buzz')
    else:
        print(vector[i])
