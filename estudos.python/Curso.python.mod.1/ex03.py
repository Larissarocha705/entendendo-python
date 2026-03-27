#// 3. Desenvolva um programa que converta uma quantia de dinheiro de dólares em euros. Solicite ao usuário o valor em dólares ea taxa câmbio atual.

valor_dolares = float(input("Insira o valor em dólares: $"))
taxa_cambio = float(input("Insira a taxa de câmbio atual (1 dólar em euros):"))
valor_euros = valor_dolores * taxa_cambio
print(f"o valor de ${valor_dolares:.2f} equivale a €{valor_euros:.2f} com a taxa de câmbio atual.")