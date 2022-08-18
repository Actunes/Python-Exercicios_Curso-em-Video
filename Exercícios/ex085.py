'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os
valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

from time import sleep
mensagem = 'Listas com pares e ímpares'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

lista = [[],[]]
for c in range (1,8):
    numero = (int(input(f'Digite o {c}º número: ').strip()))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[1].sort()
lista[0].sort()
print(f'Valores pares: {lista[0]}\nValores ímpares: {lista[1]}')
