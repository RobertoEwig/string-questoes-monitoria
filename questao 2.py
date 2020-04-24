#Faça um programa que leia um número de telefone, e corrija o número no caso
#deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode
#informar o número com ou sem o traço separador.

import sys

telefone = input("Digite um numero de telefone.\n")

contadorNumeros = 0

for i in range(0, len(telefone)):
  if telefone[i].isdigit():
    contadorNumeros += 1

if contadorNumeros == 7:
  telefone = "3" + telefone

print(telefone)