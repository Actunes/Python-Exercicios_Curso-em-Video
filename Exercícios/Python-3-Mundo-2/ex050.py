'''Desenvolva um programa que leia seis números inteiros e mostra a soma
apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('      SOMA DE PARES')
print('='*25)
print('\033[m')
sleep(0.5)
soma = 0
for c in range (1,7):
    numero = int(input('Digite o {}º número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
sleep(0.5)
print('')
print('Soma de todos os números pares: {}'.format(soma))
print('')