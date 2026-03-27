#Crie um algoritmo que leia um número e mostre o seu dobro ,seu triplo e a raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n**(1/2)
print(f'O dobro do número {n} é {d}\nO triplo do número {n} é {t}\nA sua raíz é {r:.2f}')