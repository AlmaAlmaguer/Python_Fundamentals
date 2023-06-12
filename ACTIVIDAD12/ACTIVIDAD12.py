'''
Programa que permita al usuario ingresar los montos de las compras de un cliente 
-se desconoce la cantidad de datos que se cargarán, que pueden cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingresa el monto 0.
cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad.
 informar el total a pagar, si las ventas superan el total de $1000, se debe aplicar un 10% de descuento.
'''


compra=1
total= 0 
while(compra!=0):
    compra = float(input("Ingrese el monto de compra: "))
    if(compra>0):
        total+=compra
    elif(compra<0):
        print("La compra no puede ser menor a 0 \n")
      
if(total>1000):
    total-=total*.10
print ("Su total: $", total)

     
