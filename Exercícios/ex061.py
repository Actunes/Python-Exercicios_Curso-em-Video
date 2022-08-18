'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a
estrutura while.'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('PROGRESSÃO ARITMÉTICA V2')
print('='*25)
print('\033[m')
sleep(0.5)
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contagem = 1
while contagem <= 10:
    print('{} -> '.format(termo),end = '')
    termo += razao
    contagem += 1
print('fim')