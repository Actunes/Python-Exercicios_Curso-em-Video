'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação até
ter um valor correto.'''

from time import sleep
print('\033[0;33m')
print('='*25)
print('    VALORES CORRETOS')
print('='*25)
print('\033[m')
sleep(0.5)
sexo = ''
sexo = str(input('Digite o sexo da pessoa [F/M] : ').upper())
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, digite novamente [F/M] : ').upper().strip())
print('sexo computado com sucesso')