#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento.
salario = float(input('Qual é o salário atual R$'))
aumento = salario + (salario * 15 /100)
print(f'O valor do salário atual é {salario} e o reajuste é de 15% e o novo salário é {aumento}')