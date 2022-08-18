'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais.'''

from time import sleep
mensagem = 'CONTADOR DE VOGAIS'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

tupla = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON',
         'CURSO','GRATIS','ESTUDAR','PRATICAR',
         'TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

for c in tupla:
    print(f'\nVogais de {c}: ', end='')
    for vogal in c:
        if vogal.lower() in 'aeiou':
            print(vogal,end= ' ')