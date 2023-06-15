'''
Crear una calculadora con al menos 4 operaciones básicas definiendo una clase "calculadora" y dentro de esta las operaciones (sumar, restar, dividir y multiplicar).
El programa debe pedirle al usuario que ingrese dos valores, con los cuales la calculadora hará las 4 operaciones definidas anteriormente. 
Es importante recordar que al momento de hacer una división, el denominador no puede ser igual a 0, por lo que en caso de que el usuario ingrese dicho valor, 
el programa debe imprimir que la respuesta de la operación de división con dicho valor ingresado es indefinido.
'''

import numpy 

class calculadora:
    def __init__(self, valor1, valor2):
      self.valor1 = float(valor1)
      self.valor2 = float(valor2)

    def sumar(self):
        suma = self.valor1 + self.valor2
        return suma
    
    def restar(self):
        resta = self.valor1 - self.valor2
        return resta

    def multiplicar(self):
        multiplicacion = self.valor1 * self.valor2
        return multiplicacion

    def dividir(self):
        if(self.valor2==0):
            print('La respuesta a su operación es indefinida')
            return 0 
        else:
            division= self.valor1 / self.valor2
            return division

valor1 =input('Ingrese numero 1:')
operador = input ('Ingrese operador')
valor2 = input('Ingrese numero 2:')

calculadora= calculadora (valor1,valor2)

resultado =0


match operador:
    case '+':
        resultado = calculadora.sumar()
        print('El resultado es:',resultado)
    case'-':
        resultado =calculadora.restar()
        print('El resultado es:',resultado)
    case'*':
        resultado =calculadora.multiplicar()
        print('El resultado es:',resultado)
    case'/':
        resultado = calculadora.dividir()
    case other:
        print('El operador no se encuentra disponible')



