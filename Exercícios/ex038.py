'''Escreva um programa que leia dois números inteiros
e compare-os,mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais'''

from time import sleep
print('\033[0;35m')
print('='*25)
print('  COMPARAÇÃO DE NÚMEROS')
print('='*25)
print('\033[m','\033[0;94m')
sleep(0.5)
Número_1 = int(input('Primeiro número: '))
Número_2 = int(input('Segundo número: '))
print('\033[m')
if Número_1 > Número_2:
    maior = 'O primeiro valor é maior.'
    print(maior)
elif Número_1 < Número_2:
    maior = 'O segundo valor é maior.'
    print(maior)
elif Número_1 == Número_2:
    print('Não há valor maior, ambos são iguais.')
print('')