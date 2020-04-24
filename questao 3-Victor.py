import sys
notas = []
nota = 0
b = 0
c = len(notas)+1

while nota != -1:
  nota = float(input("Insira a nota:\n"))
  notas.append(nota)

notas.remove(-1)

media = sum(notas)/len(notas)
medias = 0
mediaMsete = 0

i = 0
for i in range(0, len(notas)):
  if notas[i] >= media:
    medias += 1
    i += 1
  else: i += 1

i = 0
for i in range(0, len(notas)):
  if notas[i] <= 7:
    mediaMsete += 1
    i += 1
  else: i += 1


print(len(notas))
print(notas)
notas.reverse()
while b <= c:
  print(notas[b],"\n")
  b = b + 1 
print(sum(notas))
print(media)
print(medias)
print(mediaMsete)
sys.exit()