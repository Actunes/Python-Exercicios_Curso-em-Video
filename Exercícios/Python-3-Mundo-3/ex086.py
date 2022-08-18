'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz 
na tela, com a formatação correta.'''

from time import sleep
mensagem = 'Matriz em Python'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0,3):
        matriz[x][y] = int(input(f'Digite um valor para [{x}][{y}]: '))
print()
for x in range(0,3):
    for cy in range(0,3):
        print(f'[{matriz[x][y]:^5}]',end='')
    print()