'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da
estrutura na tela.'''

from time import sleep
mensagem = 'Dicionário em Python'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

dic = {}

dic['Nome'] = str(input('Nome do aluno: '))
dic['Média'] = float(input(f'Média do(a) {dic["Nome"]}: '))
if dic['Média'] >= 7:
    dic['Situação'] = 'Aprovado'
elif 5 <= dic['Média'] < 7 :
    dic['Situação'] = 'Recuperação'
else:
    dic['Situação'] = 'Reprovado'
print()

for k,v in dic.items():
    print(f'{k} é igual á {v}')
print()