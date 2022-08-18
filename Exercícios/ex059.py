'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa'''

from time import sleep
from unittest import result
print('\033[0;33m')
print('='*25)
print('     MENU DE OPÇÕES')
print('='*25)
print('\033[m')
sleep(0.5)
valor_1 = 0
valor_2 = 0
valor_1 = float(input('Digite um valor: '))
valor_2 = float(input('Digite outro valor: '))
print('')
escolha = 0
resultado = 0
while not escolha == 5:
    print('''[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')

    print('')
    escolha = int(input('Digite o número escolhido: '))
    print('')
    if escolha == 1:
        resultado = valor_1 + valor_2
        print('A soma entre {} e {} é {}'.format(valor_1,valor_2,resultado))
    elif escolha == 2:
        resultado = valor_1 * valor_2
        print('A multiplicação entre {} e {} é {}'.format(valor_1,valor_2,resultado))
    elif escolha == 3:
        if valor_1 > valor_2:
            resultado = valor_1
        elif valor_1 == valor_2:
            print('Os 2 valores são iguais')
        else:
            resultado = valor_2
        print('Entre {} e {}, o maior valor é {}'.format(valor_1,valor_2,resultado))
    elif escolha == 4:
        valor_1 = float(input('Digite um valor: '))
        valor_2 = float(input('Digite outro valor: '))
    else:
        print('Opção invalida, tente novamente!')
        print('')
print('Programa FINALIZADO')
print('')
