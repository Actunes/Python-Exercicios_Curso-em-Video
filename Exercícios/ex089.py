'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

from time import sleep
mensagem = 'Boletim'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

aluno = []
banco_de_dados = []

while True:
    média = 0
    aluno.append(str(input('Nome do aluno: ').strip().title()))
    aluno.append(float(input('Nota 1: ').strip()))
    aluno.append(float(input('Nota 2: ').strip()))
    média = (aluno[1] + aluno[2]) / 2
    aluno.append(média)
    banco_de_dados.append(aluno[:])
    aluno.clear()
    escolha = str((input('Deseja continuar?[s/n] ').strip().lower()))
    if escolha == 'n':
        break

print()
print('='*23)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i , a in enumerate(banco_de_dados):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
    
while True:
    print()
    escolha = int(input('Digite o número do aluno para ver as notas: (999 para sair) '))
    print()
    if escolha == 999:
        break
    if escolha <= len(banco_de_dados) - 1:
        print(f'Aluno: {banco_de_dados[escolha][0]}\nNotas: {banco_de_dados[escolha][1:3]}')
