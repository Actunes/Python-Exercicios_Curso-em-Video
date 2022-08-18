'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

from time import sleep
print('\033[0;31m')
print('='*25)
print('   CADASTRO DE PESSOA')
print('='*25)
print('\033[m')
sleep(0.5)
sexo =''
maior_18 = 0
homens = 0
mulheres_maior20 = 0
escolha_usuario = ''
while True:
    idade = int(input('Idade da pessoa: '))
    print('---------------------')
    sexo = str(input('Sexo da pessoa [M/F]: ').strip().upper())[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo da pessoa [M/F]: ').strip().upper())[0]
        if sexo == 'MF':
            break
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade >=20:
        mulheres_maior20 +=1
    print('---------------------')
    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Deseja adicionar mais pessoas? S/N ').strip().upper())[0]
    print('---------------------')
    if escolha_usuario == 'N':
        break
print(f'Pessoas maior de idade: {maior_18}\nHomens cadastrados: {homens}\nMulheres com idade superior á 20: {mulheres_maior20}')
print('')