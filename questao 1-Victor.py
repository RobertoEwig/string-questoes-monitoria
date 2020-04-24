import sys
idade = [12,13,13,16,17,18,11,12,10,21,9,11,12,13,14,12,13,13,16,17,18,11,12,10,21,9,11,12,13,14]
altura = [1.62,1.55,1.45,1.60,1.72,1.58,1.49,1.63,1.56,1.49,1.62,1.55,1.45,1.60,1.72,1.58,1.49,1.63,1.56,1.49,1.62,1.55,1.45,1.60,1.72,1.58,1.49,1.63,1.56,1.49]

medAltura = (sum(altura) / len(altura))
abaixoMed = 0
i = 0
for i in range(0, 29):
  if altura[i] <= medAltura:
    abaixoMed += 1
    i += 1
  else: i += 1

print(abaixoMed)

acimaTreze = 0
i = 0 
for i in range(0, 29):
  if idade[i] > 13: 
    acimaTreze += 1 
    i += 1 
  else: i += 1

print(acimaTreze)