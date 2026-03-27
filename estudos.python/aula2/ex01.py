#// 1.Crie um programa que classifique uma pessoa em uma das seguintes categorias com base na idade
#//criança (0-12 anos)Criança (0-12 anos)
#// Adolescente (13 a 17 anos)
#// Adulto (18-64 anos)
#//Idosos (65 anos ou mais)
idade = int(input('Digite sua idade:'))
if idade >= 0 and idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 64:
    print('Adulto')
elif idade >= 64:
    print('Idoso')
elif idade < 0:
    print('Idade Invalida')