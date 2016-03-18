#Algoritmo RSA
#Autor: David Felipe Velez Cadavid
#Estudiante de Computacion Cientifica
#Universidad de Medellin (UdM)
#Objetivo: Crear un sistema de funciones que dados p y q me generen las llaves publica y privada del algortimo RSA.


#Problema 1	

#Escriba una funcion que dados dos numeros primos p y q genere las llaves publica y privada del algoritmo RSA

#Solucion:


#En el algoritmo se determinan 3 funciones de sustento que se complementan en f(RSA) es decir, que son
#fundamentales para crear y ejecutar la cuarta funcion que genera las llaves publica y privada del RSA.

import random
import sys

#Funcion MCD

#Estrategia:
#Se utiliza el algoritmo de Euclides.
#El algoritmo se centra basicamente en dividir el numero mayor a entre el numero menor b, mientras diferente 
#de 0 y hasta que el resto de a/b sea 0, dado el caso de que a<b se aplica intercambio de valores a las variables,
#(funciona como un tipo de auxiliar que reemplaza valores).
#Devuelve el maximo comun divisor de a y b.

def Emcd(a, b):
    
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


#Funcion Numeros Primos relativos

#Estrategia:
#Dos numeros son coprimos si no tienen otro divisor comun mas que 1 y -1.
#Si los dos numeros son coprimos me retorna "True", es decir, 1.De lo contrario me retorna "False", es decir, 0.


def coprime_num (x,y):
	if Emcd(x,y) == 1:
		return 1
	else:

		return 0


#Funcion Numero Primo

#Estrategia:
#Un numero es primo si solo es divisible por el mismo numero y por 1.
#Si el numero es menor que dos me retorna no es primo por tanto me retorna 0.
#Si el numero es primo me retorna 1, de lo contrario me retorna 0.


def prime_num(num):
    if num < 2:              
	return 0
    for i in range(2, num):  
	if num % i == 0:     
	 return 0
    return 1                 


# Funcion Claves RSA

#Estrategia:
#En primera instancia se confirma que p y q son numeros primos, de lo contrario se genera un tipo de break que me 
#expulsa de la funcion.
#Si los numeros cumplen la condicion son enviados a la siguiente etapa donde se genera N equivalente a (p*q) y en 
#su efecto se genera el algoritmo de euler.
#Para hallar e correspondiente a la llave publicaexisten dos condiciones basicas:[1 < e < phi] y coprimo con phi.
#Por ello se crea una tupla que va desde 2 hasta phi sin contar phi, se implementa el modulo random.randrange que
#me genera una lista de numeros aleatoriamente con el rango y argumentos dados. Para que el modulo no se base en el
#tiempo para generar los numeros se utiliza random.seed(1) que define una instancia desde la cual siempre va actualizarce.
## El modulo requiere que se importe al file random: import random.De otro modo el programa encuentra date flotante 
#que genera error.Para hallar d correspondiente a la clave privada se utiliza de igual manera el modulo random.randrange

#Se utiliza la Funcion Numeros relativos para buscar en la lista 'e' el ultimo numero que sea coprimo con phi.

#'d' se encuentra multiplicando una lista de numeros * e, y si al dividir el producto entre phi, el residuo
#es 1, encotraremos una lista de posibles 'd'. Por tal razon se crea un ciclo en el que 'd' es una lista que 
#va desde 0 hasta phi*2 para hallar el d de la lista que me cumpla la condicion.

def rsa(p,q):
        
	random.seed(1)

	print 
        if prime_num(p) == 0 or prime_num(q) == 0:
	       	sys.exit("Error.The values entered are not numbers prime, please retry!")	
	 			
	else:
                print "Great.The entered numbers are prime numbers."
		print "Generating keys..."
		N = p * q
        	phi = (p-1)*(q-1)
		
		e=random.randrange(2,phi)
	     	if coprime_num (e,phi) == 1:
			return e	
		d=random.randrange(phi*2)
		if e * d % phi == 1:
			return d	
		print "Done..."
		print "LLave publica: ","e= ",e,',',"N= ",N #salida de llave publica
		print "LLave privada: ","d= ",d,',',"N= ",N #salida de llave privada

	

v=int(input("Ingrese el numero primo para p: "))#entrada de valor p
u=int(input("Ingrese el numero primo para q: "))#entrada de valor q

val=rsa(v,u)#evaluacion de entradas
print val



