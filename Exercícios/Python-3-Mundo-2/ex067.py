'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.'''
from time import sleep
print('\033[0;31m')
print('='*25)
print('       TABUADA V3')
print('='*25)
print('\033[m')
sleep(0.5)
escolha_usuario = int(input('Escolha um número: '))
while escolha_usuario > 0:
    for c in range (0,11):
        resultado = c * escolha_usuario
        print('{} X {} = {}'.format(c,escolha_usuario,resultado))
    print('')
    escolha_usuario = int(input('Escolha um número: '))
    print('')
    if escolha_usuario < 0:
        break
print('')