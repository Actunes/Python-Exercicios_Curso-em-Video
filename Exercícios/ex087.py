'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

from time import sleep
mensagem = 'Matriz em Python v2'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = 0 
soma_coluna = 0
maior = 0

for x in range(0,3):
    for y in range(0,3):
        matriz[x][y] = int(input(f'Digite um valor para [{x}][{y}]: '))
print()
for x in range(0,3):
    for y in range(0,3):
        print(f'[{matriz[x][y]:^5}]',end='')
        if matriz[x][y] % 2 == 0:
            soma_par += matriz[x][y]
    print()
print()
print(f'Soma de todos os valores pares: {soma_par}')
for x in range(0,3):
    soma_coluna += matriz[x][2]
print(f'Soma de todos os valores da terceira coluna: {soma_coluna}')
for y in range(0,3):
    if y == 0:
        maior = matriz[1][y]
    elif matriz [1][y] > maior:
        maior = matriz[1][y]
print(f'Maior valor da segunda coluna: {maior}')
print()        

