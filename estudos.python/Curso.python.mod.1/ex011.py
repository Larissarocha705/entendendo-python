#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessaria para pintá-la, sabendo que cada litro da tinta, pinta uma área de 2m quadrados.
altura = float(input("Qual o valor de altura da parede?"))
largura = float(input("Qual o valor da largura da parede?"))
area = altura * largura 
tinta = area / 1
print(f"O valor da aréa é {area}m² e gastará {tinta}L de tinta")