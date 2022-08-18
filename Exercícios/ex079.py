'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista 
lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

from time import sleep
mensagem = 'Valores únicos em uma Lista'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

resposta = 's'
lista = []

while resposta == 's':
    valor = int(input('Digite o valor: '))

    if valor not in lista:
        lista.append(valor)
        print('valor adicionado.')

    else:
        print('Valor duplicado, tente outro número')
    resposta = str(input('Deseja adicionar mais valores? [S/N] ')).strip().lower()
    while resposta not in 'sn':

        resposta = str(input('Opção invalida, tente novamente. [S/N] ')).strip().lower()
    if resposta == 'n':
        
        print('Programa finalizado, aguarde.')
        sleep(1)

lista.sort()

print(f'Ordem: {lista}')