'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''
from time import sleep
from math import factorial
print('\033[0;33m')
print('='*25)
print('        FACTORIAL')
print('='*25)
print('\033[m')
sleep(0.5)
número = int(input('Digite um número: '))
print('{}! = {}'.format(número,factorial(número)))
print('')