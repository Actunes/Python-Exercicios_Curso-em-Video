'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular.'''
from time import sleep
mensagem = 'LISTA DE PREÇOS'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'comprasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

for posicao in range(0,len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end = ' ')
    else:
        print(f'R$ {produtos[posicao]:.>3.2f}')
print('')