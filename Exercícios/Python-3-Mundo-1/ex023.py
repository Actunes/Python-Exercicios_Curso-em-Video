'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados.
ex: 1834
Unidade: 4 
Dezena: 4
Centena: 8
Milhar: 1'''

print('')
print('='*25)
Número = int(input('Digite um número (0-9999): '))
'''Número_String = str(Número)
Milhar = Número_String[0]
Centena = Número_String	[1]
Dezena = Número_String [2]
Unidade = Número_String [3]
print('Milhar: {}'.format(Milhar))
print('Centena: {}'.format(Centena))
print('Dezena: {}'.format(Dezena))
print('Unidade: {}'.format(Unidade))'''
Milhar = Número // 1000 % 10
Centena = Número // 100 % 10
Dezena = Número // 10 % 10
Unidade = Número // 1 % 10
print('Milhar: {}'.format(Milhar))
print('Centena: {}'.format(Centena))
print('Dezena: {}'.format(Dezena))
print('Unidade: {}'.format(Unidade))
print('')