'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from emoji import emojize
from time import sleep
print('\033[0;35m')
print('='*25)
print('   CONTAGEM REGRESSIVA')
print('='*25)
print('\033[m')
sleep(0.5)
for c in range (10,-1,-1):
    sleep(1)
    print(c)
print(emojize(':fogos_de_artifício: :fogos_de_artifício: :fogos_de_artifício:' ,language = 'pt'))