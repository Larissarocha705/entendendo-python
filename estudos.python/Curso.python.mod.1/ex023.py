#Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos dígiteos separados 
num = int(input('Informe um número: '))
U = num // 1 % 10
D = num // 10  % 10
C = num // 100 % 10
M = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(U))
print('Dezena: {}'.format(D))
print('Centena {}'.format(C))
print('Milhar {}'.format(M))