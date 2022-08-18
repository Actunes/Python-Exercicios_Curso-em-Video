'''Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três no intervalo de 1 até 500.'''

from time import sleep
print('\033[0;37m')
print('='*25)
print('SOMA DE MULTIPLOS DE TRÊS')
print('='*25)
print('\033[m')
sleep(0.5)
soma = 0
contador = 0
for c in range (1,501,2):
    if c % 3 == 0:
        soma = soma + c #soma += c
        contador = contador + 1 #contador += 1
print('Soma dos valores: {}'.format(soma))
print('Valores Solicitados: {}'.format(contador))
print('')
