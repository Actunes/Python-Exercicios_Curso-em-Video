'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
from time import sleep
print('\033[0;31m')
print('='*25)
print('    CAIXA ELETRÔNICO')
print('='*25)
print('\033[m')
sleep(0.5)
valor_sacado = 0
valor_sacado = int(input(('Digite o valor_sacado á ser sacado: R$')))
nota50 = valor_sacado // 50
valor_sacado %=  50
nota20 = valor_sacado // 20
valor_sacado %= 20
nota10 = valor_sacado // 10
valor_sacado %= 10
nota1 = valor_sacado // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")