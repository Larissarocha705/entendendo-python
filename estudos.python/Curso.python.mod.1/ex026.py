#Faça um progrma que leia uma frase pelo teclado e mostre. Quantas veses aparece a letra 'A' . Em que sua posição inicial aparece a primeira vez.Em que posição ela aparece na ultima vez.
frase = str(input('Digite uma frase: ')).lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))