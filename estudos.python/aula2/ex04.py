#//4.Crie um programa que classifique as notas de um aluno em duas disciplinas e imprima se o aluno for aprovado em ambas as disciplinas.
#//O aluno é aprovado se obtiver nota igual ou superior a 60 em cada disciplina.
#//Caso o aluno falte em alguma delas, poderá realizar exame de nivelamento. Se for o caso, imprima que deve fazer a prova da disciplina específica.
#//Se perder ambas, deverá imprimir reprovado.
#//A faixa de pontuação é de 0 a 100.
nota_disciplina1 = float(input('Digite a nota da primeira disciplina (0 a 100):'))
nota_disciplina2 = float(input('Digite a nota da segunda disciplina (0 a 100):'))
if 0 <= nota_disciplina1 <= 100 and 0 <= nota_disciplina2 <= 100:
    if nota_disciplina1 >= 60 and nota_disciplina2 >= 60:
        print('Aluno aprovado em ambas as disciplinas!')
    elif nota_disciplina1 < 60 and nota_disciplina2 >= 60:
        print('Aluno deve fazer o exame de nivelamento na primeira disciplina.')
    elif nota_disciplina1 > 60 and nota_disciplina2 >= 60:
        print('Aluno deve fazer o exame de nivelamento na segunda disciplina.')
    elif nota_disciplina1 < 60 and nota_disciplina2 < 60:
        print('Aluno reprovado, deve fazer o exame de nivelamento em ambas as disciplinas.')
else:
    
    print('Nota inválidas. Por favor, insira valors entre 0 e 100.')