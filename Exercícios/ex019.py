'''um professor quer sortear um dos seus quatro alunos 
para apagar o quadro, faca um programa que ajude ele
lendo o nome deles e escrevendoo nome do
escolhido'''
print('')
print('='*25)
from random import choice
Primeiro_Aluno = str(input('Primeir Aluno: '))
Segundo_Aluno = str(input('Segundo Aluno: '))
Terceiro_Aluno = str(input('Terceiro Aluno: '))
Quarto_Aluno = str(input('Quarto Aluno: '))
lista = [Primeiro_Aluno,Segundo_Aluno,Terceiro_Aluno,Quarto_Aluno]
Aluno_Escolhido = choice(lista)
print('Aluno Escolhido: {}'.format(Aluno_Escolhido))
print('')
