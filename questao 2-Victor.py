import sys
dadosSalto = []
nome = input("Insira o nome do competidor\n")
if nome is None:
  sys.exti()
else:
  s1 = float(input("Insira o valor do primeiro salto.\n"))
  dadosSalto.insert(0, s1)
  s2 = float(input("Insira o valor do segundo salto.\n"))
  dadosSalto.insert(1, s2)
  s3 = float(input("Insira o valor do terceiro salto.\n"))
  dadosSalto.insert(2, s3)
  s4 = float(input("Insira o valor do quarto salto.\n"))
  dadosSalto.insert(3, s4)
  s5 = float(input("Insira o valor do quinto salto.\n"))
  dadosSalto.insert(4, s5)

medSalto = sum(dadosSalto)/len(dadosSalto)

print("Resultado final: ")
print("Atleta: ", nome)
print("Saltos", dadosSalto[0], "-", dadosSalto[1], "-", dadosSalto[2],"-", dadosSalto[3],"-", dadosSalto[4])
print("Média de saltos:", medSalto,"m")
