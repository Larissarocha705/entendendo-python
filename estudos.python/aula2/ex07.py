
#//7.Projete um programa que simule as operações de um caixa eletrônico. Permite ao usuário fazer depósitos, saques e consultar saldo. Use loops while para manter a interação até que o usuário decida sair.
saldo = 0.0
while True:
    print("\nBem-vindo ao Caixa Eletrônico!")
    print("1. Consultar saldo")
    print("2. Fazer depósito")
    print("3. Fazer saque")
    print("4. Sair")
    opcao = input("Escolha uma opção (1-4): ")
    if opcao == '1':
        print(f"Seu saldo é: R$ {saldo:.2f}")
    elif opcao == '2':
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")
    elif opcao == '3':
        valor_saque = float(input("Digite o valor a ser sacado: R$ "))
        if 0 < valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        elif valor_saque > saldo:
            print("Saldo insuficiente para saque.")
        else:
            print("Valor de saque inválido.")
    elif opcao == '4':
        print("Obrigado por usar o Caixa Eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")