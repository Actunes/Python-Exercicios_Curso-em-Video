'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
from time import sleep
print('\033[0;35m')
print('='*25)
print('   CONTAGEM REGRESSIVA')
print('='*25)
print('\033[m')
sleep(0.5)
for c in range (1,51):
    if c % 2 == 0:
        print(c, end = ' ')