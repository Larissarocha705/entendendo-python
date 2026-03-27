#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Qual o valor do produto desejado: R$'))
desconto = (valor * 0.5 /100) + valor 
print(f'O valor do produto é de {desconto} com o desconto de 5%') 