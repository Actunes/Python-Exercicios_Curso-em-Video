''''O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos.Faca
um programa que leia o nome dos quatro alunos e mostre
a ordem sorteada.'''
print('')
print('='*25)
from random import shuffle
Primeiro_Aluno = str(input('Primeir Aluno: '))
Segundo_Aluno = str(input('Segundo Aluno: '))
Terceiro_Aluno = str(input('Terceiro Aluno: '))
Quarto_Aluno = str(input('Quarto Aluno: '))
Lista = [Primeiro_Aluno,Segundo_Aluno,Terceiro_Aluno,Quarto_Aluno]
shuffle(Lista)
print(Lista)
print('')