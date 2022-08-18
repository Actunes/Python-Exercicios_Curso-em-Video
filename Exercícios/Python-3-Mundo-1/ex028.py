'''Escreva um programa que faça o computador
''pensar'' em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o escolhido
pelo computador.
O programa deverá escrevar na telas se o usuario 
vendeu ou perdeu.'''
from random import randint
import emoji
from time import sleep

print('')
print('='*25)
print('')
Número_Usuário = int(input('Em que número pensei? (0:5) > '))
Número_Maquina = randint(0,5)
print('')
sleep(2)
if Número_Usuário == Número_Maquina:
    print(emoji.emojize('Parabéns, você acertou o número!! :cone_de_festa: ',language='pt'))
else:
    print(emoji.emojize('Infelizmente você errou o número :rosto_triste_mas_aliviado: , eu pensei no múmero {}!'.format(Número_Maquina),language='pt'))
print('')
