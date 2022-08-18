'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser
que quer mostrar 0 termos.'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('PROGRESSÃO ARITMÉTICA V3')
print('='*25)
print('\033[m')
sleep(0.5)
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contagem = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contagem <= total:
        print('{} -> '.format(termo),end = '')
        termo += razao
        contagem += 1
    print('pausa')
    mais = int(input('Termos a mais: '))
print('finalizado com {} termos'.format(total))