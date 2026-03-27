#// 2. Crie um programa que solicite ao usuário o valor total de sua compra. Aplique um desconto de 10% no total da compra.Imprima o valor após o desconto.

valor_compra = float(input("Insira o valor total da sua compra: R$"))
desconto = valor_compra * 0.10
valor_final = valor_compra - desconto 
print(f"o valor após o desconto de 10% é:R$ {valor_final:.2f}")

