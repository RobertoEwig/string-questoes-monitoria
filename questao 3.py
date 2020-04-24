#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do
#seu comprimento. Informe também se as duas strings possuem o mesmo
#comprimento e são iguais ou diferentes no conteúdo. Obs: não utilize
#nenhuma biblioteca como por exemplo len() ou ‘==’ para realizar
#comparação.

import sys

def tamanhoString(str):
  count = 0

  for s in str:
    count += 1

  return count

def comprimetoString(str1, str2):
  if tamanhoString(str1) != tamanhoString(str2):
    return "Tamanhos diferentes"
  else:
    return "Tamanhos iguais"

def conteudoString(str1, str2):
  if tamanhoString(str1) != tamanhoString(str2): 
    return "Conteudos diferentes";
  else:
    for i in range(0, tamanhoString(str1)):
      if str1[i] != str2[i]:
        return "Conteudos diferentes"
      
    return "Conteudos iguais"

str1 = input("Informe a primeira string\n")
str2 = input("Informe a segunda string\n")

resultado = comprimetoString(str1, str2)

print(resultado)

resultado = conteudoString(str1, str2)

print(resultado)