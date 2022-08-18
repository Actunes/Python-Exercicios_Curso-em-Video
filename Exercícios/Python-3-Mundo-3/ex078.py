'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado 
e as suas respectivas posições na lista.'''

from time import sleep
mensagem = 'Maior e Menor valores na Lista'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

lista = []
pos_menor = []
pos_maior = []
for cont in range (0,5):
    lista.append(int(input(f'Digite o {cont} valor: ')))
for pos,valores in enumerate(lista):
    if valores == max(lista):
        pos_maior.append(pos)
    if valores == min(lista):
        pos_menor.append(pos)
print(f'Valores digitados: {lista}')
print(f'Maior valor: {max(lista)} Posição: {pos_maior}\nMenor valor: {min(lista)} Posição: {pos_menor}')
print()