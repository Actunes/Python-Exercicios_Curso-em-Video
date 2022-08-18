'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas 
os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

from time import sleep
mensagem = 'Dividindo valores em várias listas'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

resposta = 's'
lista = []
lista_impar = []
lista_par = []

while resposta == 's':
    valor = int(input('Digite o valor: '))
    lista.append(lista)
    if (valor % 2) == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    resposta = str(input('Deseja adicionar mais valores? [S/N] ')).strip().lower()
    while resposta not in 'sn':
        resposta = str(input('Opção invalida, tente novamente. [S/N] ')).strip().lower()
    if resposta == 'n':
        sleep(1)
        print('Programa finalizado, aguarde.')
        sleep(1)

print(f'Valores digitados: {lista}\nValores pares: {lista_par}\nValores ímpares: {lista_impar}')