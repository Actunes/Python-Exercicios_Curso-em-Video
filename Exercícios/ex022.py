'''Crie um programa que leia o nome completo de uma
pessoa e mostre:
O nome com todas as letras maiusculas
O nome com todas minusculas
Quantas letras ao todo(Sem considerar espacos)
Quantas letras tem o primeiro nome'''

print('')
print('='*25)
nome = str(input('Digite seu nome completo: ')).strip()
nome_maisculas = nome.upper()
nome_minusculas = nome.lower()
nome_letras = len(nome) - nome.count(' ')
#separa = nome.find(' ') 
separa = nome.split()
nome_first = len(separa[0])
print('Seu nome em Maisculas: {}'.format(nome_maisculas))
print('Seu nome em Minusculas: {}'.format(nome_minusculas))
print('Seu nome tem: {} Letras'.format(nome_letras))
print('Seu primeiro nome tem: {} Letras'.format(nome_first))
print('')