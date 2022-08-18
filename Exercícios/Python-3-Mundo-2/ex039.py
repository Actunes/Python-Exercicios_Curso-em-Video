'''Faça um programa que leia o ano de nascimento
de um jovem e informe de acordo com sua idade:
-Se ele ainda vai se alistar ao servico militar.
-Se é a hora de se alistar
-Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que 
falta ou que passou do prazo.'''
from datetime import date
from time import sleep
print('\033[0;35m')
print('='*25)
print('       ALISTAMENTO')
print('='*25)
print('\033[m')
sleep(0.5)
year = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
alistamento = year - ano_nascimento
if alistamento >= 19:
    print('Já passou do tempo de alistamento!')
    print('Anos excedentes: {} anos'.format(alistamento - 18))
elif alistamento <= 16:
    print('Voce ainda vai se alistar ao servico militar!')
    print('Anos faltantes: {} anos'.format(18 - alistamento))
elif alistamento == 18 or 17:
    print('Está na hora de se alistar ao servico militar!')
print('')