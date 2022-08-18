'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''

import datetime
from time import sleep
print('\033[0;33m')
print('='*25)
print('       MAIORIDADE')
print('='*25)
print('\033[m')
sleep(0.5)
#contagem
maior = 0 
menor = 0
#pega o ano atual em int e subtrai 18
data = datetime.date.today()
ano_atual = int(data.strftime('%Y'))
#ano_menor = ano_atual - 18
#verifica as 7 datas de nascimento e soma na contagem
for c in range (1,8):
    ano_nascimento = int(input('Data de nascimento da {}ª pessoa: '.format(c)))
    if  ano_atual - ano_nascimento >= 18:
        maior += 1
    else:
        menor += 1
print('')
print('Pessoas que atingiram a maioridade: {}\nPessoas que não atingiram a maioridade: {}'.format(maior,menor))
print('')