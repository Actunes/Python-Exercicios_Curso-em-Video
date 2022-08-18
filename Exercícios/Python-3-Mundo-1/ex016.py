'''Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela a sua porção inteira
ex: 6.127 = 6'''
print('')
print('='*25)
from math import trunc
número = float(input('Digite um número para mostrar a sua porção inteira: '))
print('Porção Inteira: {}'.format(trunc(número)))
print('')
