'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total 
de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
from time import sleep
print('\033[0;31m')
print('='*25)
print('      PAR OU IMPAR')
print('='*25)
print('\033[m')
sleep(0.5)
numero_jogador = 0
numero_computador = 0
escolha = ''
resultado = 0
numero_computador = randint(1,10)
soma = 0
resultado = 0
pontos = 0
while True:
    numero_jogador = int(input('Digite o número: '))
    escolha = str(input('Digite sua escolha [P/I]: ').upper().strip())
    while escolha not in 'PI':
        escolha = str(input('Digite sua escolha [P/I]: ').upper().strip())
    if escolha == 'P':
        soma = numero_jogador + numero_computador
        if soma % 2 == 0:
            print(f'Número escolhido pela maquina: {numero_computador}')
            print('Parabéns, você venceu! +1 ponto')
            pontos += 1
        else:
            break
    elif escolha == 'I':
        soma = numero_jogador + numero_computador
        if soma % 2 == 1:
            print(f'Número escolhido pela maquina: {numero_computador}')
            print('Parabéns, você venceu! +1 ponto')
            pontos += 1
        else:
            break
print(f'Vitórias consequitivas: {pontos}')
        


