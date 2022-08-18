'''Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.'''
from time import sleep
print('\033[0;31m')
print('='*25)
print('       TABUADA V2')
print('='*25)
print('\033[m')
sleep(0.5)
escolha_usuario = int(input('Escolha um número: '))
print('')
sleep(0.5)
for c in range (0,11):
    resultado = c * escolha_usuario
    print('{} X {} = {}'.format(c,escolha_usuario,resultado))
print()
