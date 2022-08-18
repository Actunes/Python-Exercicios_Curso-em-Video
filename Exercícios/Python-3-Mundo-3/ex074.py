'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão na tupla.'''

from time import sleep
from random import randint
mensagem = 'NÚMEROS ALEATORIOS'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print('')
sleep(1)
tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Números sorteados:', end = '')
for c in tupla:
    print(f' {c}', end ='')
print()
print(f'\nMaior Número: {max(tupla)}')
print(f'Menor Número: {min(tupla)}')
print()