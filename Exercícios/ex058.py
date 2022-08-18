'''Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar,mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
print('\033[0;33m')
print('='*25)
print(' JOGO DE ADIVINHAÇÃO V2')
print('='*25)
print('\033[m')
sleep(0.5)
palpites = 0
número_maquina = randint(0,11)
número_escolha = int(input('Escolha um número entre 0 e 10: '))
while número_escolha != número_maquina:
    número_escolha = int(input('Você errou, digite outro número: '))
    palpites += 1
print('')
print('Parabéns, você acertou!\nNúmero escolhido: {}\nPalpites necessários: {}'.format(número_maquina,palpites))
print('')