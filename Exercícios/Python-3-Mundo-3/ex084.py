'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

from time import sleep
mensagem = 'análise de dados'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

pessoas = []
pessoas_cadastrados = []
pessoa_pesada = []
pessoa_leve = []
resposta = 's'
maior = menor = 0

while resposta == 's':
    pessoas.append(str(input('Nome: ')).strip())
    pessoas.append(int(input('Peso: ')))
    
    if len(pessoas_cadastrados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    pessoas_cadastrados.append(pessoas[:])
    pessoas.clear()
    resposta = str(input('Deseja adicionar mais pessoas? [S/N] ')).strip().lower()

    while resposta not in 'sn':
        resposta = str(input('Deseja adicionar mais pessoas? [S/N] ')).strip().lower()
    if resposta == 'n':
        break

for c in pessoas_cadastrados:
    if c[1] == maior:
        pessoa_pesada.append(c[0])
    if c[1] == menor:
        pessoa_leve.append(c[0])

print()
print(f'Números de pessoas cadastradas: {len(pessoas_cadastrados)}')
print(f'Pessoa mais leve: {pessoa_leve} com {menor}KG\nPessoa mais pesada: {pessoa_pesada} com {maior}KG')


    


