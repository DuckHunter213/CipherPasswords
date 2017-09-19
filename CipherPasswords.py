import string
import random

def generarRandom():
	numeroAleatorio = 0
	numeroAleatorio += random.randint(1,9)
	return numeroAleatorio


def cambiarLetras(cadena):
	cadenaCambiada = ""
	number = generarRandom()
	for x in cadena:
		cadenaCambiada += chr(ord(x) - number)
		cadenaCambiada += chr(ord(x) + number)
		cadenaCambiada += chr(ord(x) + ord(x))
	cadenaCambiada += "+" + str(number)
	return cadenaCambiada

def retornarLetras(cadena):
	cadena1 =""
	cadena2 =""
	number = int(cadena[len(cadena)-1:])
	print(number)
	for x in range(0,len(cadena),3):
		cadena1 += chr(ord(cadena[x])+number)
	for x in range(1,len(cadena),3):
		cadena2 += chr(ord(cadena[x])-number)
	cadena1 = (cadena1[:len(cadena1)-1])
	cadena2 = (cadena2[:len(cadena2)-1])
	print (cadena1)
	print (cadena2)
	if (cadena1 == cadena2):
		return cadena1
	else:
		return "Error al Desencriptar"

print("Que deseas hacer")
print("1.- Encriptar")
print("2.- Desencriptar")
accion = int(input())
if accion <= 1:
	print("Introduce tu cadena de texto")
	cadena = input()
	encriptado = ""
	encriptado = cambiarLetras(cadena).strip()
	print("Tu encriptado es:",encriptado)
else:
	print("Introduce tu cadena de criptografia")
	cadena = input()
	desEncriptado = ""
	desEncriptado = retornarLetras(cadena).strip()
	print("El normal es:", desEncriptado)