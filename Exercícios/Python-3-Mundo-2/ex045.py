'''Crie um programa que façã o computador jogar Jokenpô
com você.'''

import random
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']

a = str(input("PEDRA, PAPEL ou TESOURA? ")).strip().upper()
b = str(random.choice(lista))


while (a not in lista) or a == b:
    if a not in lista:
        print('\nERRO!\n')
        a = str(input("PEDRA, PAPEL ou TESOURA? ")).strip().upper()
    elif a == b:
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.3)
        print('PO!')
        print('Escolha do computador: {}.'.format(b))
        print('\nEMPATE! Jogue novamente.')
        a = str(input("PEDRA, PAPEL ou TESOURA? ")).strip().upper()
        b = str(random.choice(lista))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.3)
print('PO!')



if a == 'PAPEL' and b == 'PEDRA':
    print('\nEscolha do computador: {}.'.format(b))
    print('PARABÉNS! Você ganhou!')
else:
    if a == 'TESOURA' and b == 'PAPEL':
        print('\nEscolha do computador: {}.'.format(b))
        print('PARABÉNS! Você ganhou!')
    else:
        if a == 'PEDRA' and b == 'TESOURA':
            print('\nEscolha do computador: {}.'.format(b))
            print('PARABÉNS! Você ganhou!')
        else:
            print('\nEscolha do computador: {}.'.format(b))
            print('Você PERDEU!')