'''Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando espaços.'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('        POLÍNDROMO')
print('='*25)
print('\033[m')
sleep(0.5)
frase = str(input('Digite uma frase: ').upper().strip().replace(' ',''))
if frase == frase[::-1]: #primeiro : representa o começo da frase, o segundo : representa o final da frase
    print('A frase é um Políndromo')
else:
    print('A frase não é um Políndromo')
