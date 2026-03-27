#//  5. Escreva um programa que solicite ao usuário o peso (em quilogramas) e a altura (em metros) e calcule o IMC. 
#//IMC = peso /(altura ^ 2)
peso = float(input("Insira o seu peso (em Kg):"))
altura = float(input("Insira a sua altura (em metros):"))
imc = peso / (altura **2)
print(f"Seu IMC é: {imc:.2f}")