'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
 No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
from time import sleep
print('\033[0;31m')
print('='*25)
print(' ESTATISTICA DE PRODUTO')
print('='*25)
print('\033[m')
sleep(0.5)
escolha = ''
total_gasto = 0
mais1000 = 0
produto_barato = ''
contagem = 0
menor = 0
while True:
    nome_produto = str(input('Nome do produto: ').strip().title())
    preco_produto = float(input('Preço do produto: R$').strip())
    total_gasto += preco_produto
    if preco_produto >= 1000:
        mais1000 += 1
    if contagem == 1 or preco_produto < menor:
        menor = preco_produto
        produto_barato = nome_produto
    print('---------------------')
    escolha = str(input('Deseja adicionar mais produtos? S/N ').strip().upper())
    while escolha not in 'SN':
        escolha = str(input('Deseja adicionar mais produtos? S/N ').strip().upper())
    if escolha == 'N':
        break
print(f'Total gasto: {total_gasto}\nNúmero de produtos custando mais dde R$1000: {mais1000}\nProduto mais barato: {produto_barato}')