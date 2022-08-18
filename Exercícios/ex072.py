'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá 
ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
from time import sleep
print('\033[0;31m')
print('='*25)
print('   NUMERO POR EXTENSO')
print('='*25)
print('\033[m')
sleep(0.5)
ler = 0
numero =('zero', 'um' ,'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito' ,'nove', 'dez' ,'onze' ,'doze' ,'treze',
         'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    ler = int(input('Digite um número entre 0 e 20: '))
    if 0 <=ler <= 0:
        break
print()
print(f'Você digitou o número {numero[ler]}.')
print()