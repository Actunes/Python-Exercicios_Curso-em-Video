'''Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou IMPAR.'''

print('')
print('='*25)
print('')
Número_Inteiro = int(input('Digite um número inteiro: '))
Calculo = Número_Inteiro % 2
if Calculo == 0:
    print('O seu número é PAR!')
else:
    print('O seu número é IMPAR!')
print('')