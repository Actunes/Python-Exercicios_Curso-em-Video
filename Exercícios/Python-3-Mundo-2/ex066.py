'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é 
a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
print('\033[0;33m')
print('='*25)
print('         FLAGS')
print('='*25)
print('\033[m')
print('')
digitados = 0
soma = 0
numero = 0
while True:
    numero = int(input('Digite o número: '))
    if numero == 999:
        break
    digitados += 1
    soma += numero
print('')
print(f'Números digitados: {digitados}\nSoma dos números: {soma}') 
print('')
