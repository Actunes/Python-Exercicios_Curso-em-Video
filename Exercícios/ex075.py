'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

from time import sleep
mensagem = 'ANÁLISE DE DADOS'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)
valor = (int(input('Digite o 1º valor: ')),
         int(input('Digite o 2º valor: ')),
         int(input('Digite o 3º valor: ')),
         int(input('Digite o 4º valor: ')))
print()
print(f'Valores digitados: {valor}')
print(f'Vezes em que aparece o valor 9: {valor.count(9)}')
if 3 in valor:  
    print(f'Posição do primeiro valor 3: {valor.index(3) + 1}')
else:
    print('Posição do primeiro valor 3: ND')
print(f'Valores pares digitados: ',end='')
for c in valor:
    if c % 2 == 0:
        print(c, end = ' ')
print()