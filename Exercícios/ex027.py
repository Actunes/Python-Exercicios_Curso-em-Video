'''Faça um programa que leia o nome completo de uma
pessoa,mostrando em seguida o primeiro e o ultimo nome
separadamente
ex: Ana Maria de Souza
Primeiro = Ana
último = Souza'''

print('')
print('='*25)
Nome = str(input('Digite seu nome Completo: ')).strip().title().split()
print('Primeiro Nome: {}'.format(Nome[0]))
print('Ultimo Nome: {}'.format(Nome[len(Nome)-1]))
