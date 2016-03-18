#Desencriptacion RSA
#Autor:
#David Felipe Velez Cadavid
#Estudiante Computacion Cientifica
#Universidad de Medellin(UdM)


#Problema 2

#Escriba una funcion que dada la clave publica y un mensaje compuesto de cuatro digitos desencripte el mensaje formado 
#por estos cuatro numeros.

import random

#se crea una funcion para definir si un numero es primo
def prime_num(num):
                   
	
    for i in range(2, num):  
	if num % i == 0:    
	 return 0
    return 1


#creo una funcion que me desencriptara el mensaje cifrado
#en esta funcion se procesan e, N y los cuatro numeros dados por el usuario.
def hackrsa (e, N, n1, n2, n3, n4):
		
	for p in range(2,N):#basicamente lo que hacemos es buscar en un rango de 2 a N-1 un p que sea primo tal que el resto sea 1
		for q in range(2,N):#Buscamos un numero en el rango 2 a N-1 primo tal que el resto sea 1
			if prime_num(p)==1 and prime_num(q)==1:      
				if p * q == N:
					phi = (p-1) * (q-1)# algoritmo de euler se necesita hallar para encontrar e y d.
		

	for d in range(phi):#me genera un rango de 0 a phi-1

		if e * d % phi == 1:#me genera una condicion que dice que e por d y modulo de phi debe ser modulo de phi.
				d # me returna d es equivalente a decir return d
				m1 = n1**d%N #toma el primer digito ingresado y lo eleva a la d(sacado del rango y condicional anteriores) 						     modulo de N.
				m2 = n2**d%N # con segundo valor "" ""
				m3 = n3**d%N # con tercer valor "" ""
				m4 = n4**d%N # con cuarto valor "" ""
				
				print "mensaje desencriptado"
			        print m1,m2,m3,m4
				print "solo para fines educativos !!"

e=(input ("Por favor ingrese el valor de (e) de la LLave publica generada: " ))
N=(input ("Por favor ingrese el valor de (N) de la LLave publica generada: "))




m1=(input ("Ingrese el primer digito a desencriptar: ")) 
m2=(input ("Ingrese el segundo digito a desencriptar: "))
m3=(input ("Ingrese el tercer digito a desencriptar: "))
m4=(input ("Ingrese el cuarto digito a desencriptar: "))


finAl=hackrsa (e, N, m1, m2, m3, m4)
print finAl








