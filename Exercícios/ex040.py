'''Crie um programa que leia duas notas de um aluno
e calcule suas média,mostrando uma mensagem no final, 
de acordo com a média atingida:

-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO'''
from emoji import emojize
from time import sleep
print('\033[0;35m')
print('='*25)
print('         MÉDIA')
print('='*25)
print('\033[m')
sleep(0.5)
Primeira_Nota = float(input('Primeira nota: '))
Segunda_Nota = float(input('Segunda nota:' ))
Média = (Primeira_Nota + Segunda_Nota) /2
print()
sleep(0.4)
if Média <= 5.0:
    print('\033[0;91mAluno REPROVADO!\033[m')
elif Média >= 5.0 and Média <= 6.9:
    print('\033[0;93mAluno em RECUPERAÇÃO!\033[m')
elif Média >= 7.0:
    print('\033[0;96mAluno APROVADO!\033[m')
print('')