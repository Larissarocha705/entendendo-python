#//5.Crie um programa no qual o computador escolhe um número aleatório entre 1 e #//100 e depois pede ao usuário que adivinhe o número. Fornece pistas que #//#/indicam se o número a ser adivinhado é maior ou menor. Use um loop while #//até que o usuário adivinhe corretamente.
import random
numero_aleatorio = random.randint(1, 100)
tentativa = None
print("Tente adivinhar o número que estou pensando! (Está entre 1 e 100)")
while tentativa != numero_aleatorio:
    tentativa = int(input("Digite sua tentativa: "))
    if tentativa < numero_aleatorio:
        print("O número é maior! Tente novamente.")
    elif tentativa > numero_aleatorio:
        print("O número é menor! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número.")