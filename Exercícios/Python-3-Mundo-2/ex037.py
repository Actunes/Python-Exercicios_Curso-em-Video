'''Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual
será a base da conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

from time import sleep
print('\033[0;36m')
print('='*25)
print('   CONVERSOR DE BASES')
print('='*25)
print('\033[m','\033[0;93m')
sleep(0.5)
Número_Usuário = int(input('Digite o número inteiro: '))
print('\033[m')
sleep(0.5)
print('\033[0;97mOpções para conversão:\n[1] Binário\n[2] Octal\n[3] Hexadecimal')
print('\033[m', '\033[0;90m')
Opção = int(input('Escolha uma opção: '))
print('\033[m')
if Opção == 1:
    Valor_Convertido = bin(Número_Usuário)
    converção = 'Binário'
    print('Valor {} Convertido para {} : {}'.format(Número_Usuário,converção,Valor_Convertido))
elif Opção == 2:
    Valor_Convertido = oct(Número_Usuário)
    converção = 'Octal'
    print('Valor {} Convertido para {} : {}'.format(Número_Usuário,converção,Valor_Convertido))
elif Opção == 3:
    Valor_Convertido = hex(Número_Usuário)
    converção = 'Hexadecimal'
    print('Valor {} Convertido para {} : {}'.format(Número_Usuário,converção,Valor_Convertido))
else:
    print('Opção INVALIDA, tente novamente.')
print('')