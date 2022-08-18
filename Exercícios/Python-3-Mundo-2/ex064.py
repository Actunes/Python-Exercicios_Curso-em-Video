'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)'''

from time import sleep
print('\033[0;33m')
print('='*25)
print('    TRATANDO VALORES')
print('='*25)
print('\033[m')
print('')
'''soma = 0
números_digitados = 0
número = 0'''
soma = números_digitados = número = 0
while número != 999:
    número = int(input('Digite o valor [999 para parar]: '))
    números_digitados += 1
    soma = soma + número
    soma_2 = soma - 999
print('')
print('SOMA DE TODOS OS VALORES: {}\nNÚMEROS DIGITADOS: {}'.format(soma_2,números_digitados - 1))
print('')
