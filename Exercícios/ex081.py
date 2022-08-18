'''rie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente. 
C) Se o valor 5 foi digitado e está ou não na lista.'''

from time import sleep
mensagem = 'Extraindo dados de uma Lista'
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
        sleep(1)
        print('Programa finalizado, aguarde.')
        sleep(1)
numeros_digitados = len(lista)
lista.sort(reverse = True)
print(f'Números digitados na lista: {numeros_digitados}')
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O número 5 está na lista')
else:
    print(f'O número 5 não está na lista')