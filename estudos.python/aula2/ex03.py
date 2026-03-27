#//3.Crie um programa que determine o tipo de triângulo (equilátero, isósceles ou escaleno) com base no comprimento de seus lados.
lado1 = float(input('Digite o comprimento do lado 1:'))
lado2 = float(input('Digite o comprimento do lado 2:'))
lado3 = float(input('Digite o comprimento do lado 3:'))
if (lado1 + lado2 > lado3) and (lado1 + lado3> lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print('Triângulo equilátero (todos os lados iguais).')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo isósceles (dois lados iguais).')
    elif lado1 != lado2 != lado3:
        print('Triângulo escaleno (todos os lados diferentes).')
    else:
        print('Não é um triângulo válido')
