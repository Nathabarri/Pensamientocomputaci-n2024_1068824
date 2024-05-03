#Ejercicio No.1, Tipo de triangulo
#print("Ingrese lado 1")
#lado1= str(input())
#print("ingrese lado 1")
#lado2= str(input())
#print("Ingrese lado 3")
#lado3= str(input())

#def triangulo(lado1,lado2,lado3):
    
    #if(lado1==lado2==lado3):
     #return "Equilatero"

    #elif (lado1==lado2 or lado2 ==lado3 or lado1==lado3): 
        #return "Isoceles"  

    #else: (lado1!=lado2!=lado3)
    #return "escaleno" 

   
   
     

#print("el triangulo ingresado es:" + triangulo(lado1,lado2,lado3))

 #EJERCICIO NO.2
import math

print("Ingrese el radio:")
radio= int(input())

def ObtenerPerimetro(r):
     perimetro= float (2*r)*math.pi
     return perimetro
print("Perimetro:"+ str(ObtenerPerimetro(radio)))

def ObtenerArea(r):
    Area= float (r**2)*math.pi
    return Area
print("Area"+str(ObtenerArea(radio)))

def ObtenerVolumen(r):
 Volumen=float (4*math.pi*r**3/3)
 return Volumen
print("Volumen:"+str(ObtenerVolumen(radio)))




