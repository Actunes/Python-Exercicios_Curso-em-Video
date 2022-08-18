'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from time import sleep
from random import randint
mensagem = 'Palpites para a Mega Sena'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

palpite = []
jogos = []
numero_palpites = int(input('Número de jogos para palpite: ').strip())
print()
total = 1
while total <= numero_palpites:
    contagem = 0
    while True:
        numero = randint(0,60)
        if numero not in palpite:
            palpite.append(numero)
            contagem += 1
        if contagem >= 6:
            break
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()
    total += 1

for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print()