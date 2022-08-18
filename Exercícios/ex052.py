''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('      NÚMERO PRIMO')
print('='*25)
print('\033[m')
sleep(0.5)
Número = int(input('Digite um número inteiro: '))
total = 0
for c in range (1,Número+1):
    if Número % c == 0:
        print('\033[0;33m',end =' ')
        total += 1
    else:
        print('\033[0;31m',end =' ')
    print('{}'.format(c),end=' ')
if total == 2:
    print('Número PRIMO')
else:
    print('Não é um número PRIMO')
print('')