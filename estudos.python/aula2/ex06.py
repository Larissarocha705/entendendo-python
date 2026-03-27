#//6.Escreva um programa que conte o número de vogais de uma palavra digitada pelo usuário. Ele usa um loop for para iterar cada caractere da palavra.
palavra = input('Digite uma palavra:')
contador_vogais = 0
vogais = 'aeiouAEIOU'
for letra in palavra:
    if letra in vogais:
        contador_vogais +=1
print(f"A palavra '{palavra}' contém {contador_vogais} vogais")