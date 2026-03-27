#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço .Sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
km = float(input('Quantos Km foram percorridos: '))
dias = int(input('Quantos dias vai precisar alugar: '))
valor = (dias * 60)+ (km * 0.15)
print(f'O valor do alguel do carro ficará R${valor}')