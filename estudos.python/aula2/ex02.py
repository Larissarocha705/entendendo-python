#// 2. Implemente um programa que calcule o desconto aplicado em uma compra, considerando as seguintes regras:
#//Se o valor da compra for maior ou igual a $100, será aplicado um desconto de 10%.
#//Se o valor da compra for maior ou igual a $200, será aplicado um desconto de 20%.
compra = float(input('Digite o valor da compra: '))
if compra >= 200:
    desconto = compra * 0.20
elif compra >= 100:
    desconto = compra * 0.10
else:
    desconto = 0
print(f'Desconto aplicado: R${desconto:.2f}')
print(f'Valor final a pagar: R$ {valor_final:.2f}')