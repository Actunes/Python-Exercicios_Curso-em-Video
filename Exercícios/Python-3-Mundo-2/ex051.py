'''Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressão'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('  PROGRESSÃO ARITMÉTICA')
print('='*25)
print('\033[m')
sleep(0.5)
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
for c in range (primeiro_termo, primeiro_termo + 10 * razao,razao):
    print(c)
