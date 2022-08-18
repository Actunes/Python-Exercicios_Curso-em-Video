'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
 Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('     FIBONACCI')
print('='*25)
print('\033[m')
print('')
número = int(input('Digite um número'))
termo_1 = 0
termo_2 = 1
print('{} - {}'.format(termo_1,termo_2),end = '')
contador = 3
while contador <= número:
    termo_3 = termo_1 + termo_2
    print('- {}'.format(termo_3),end = '')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1 
print('- fim')