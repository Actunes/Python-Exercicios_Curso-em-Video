'''Crie um programa que leia o nome de uma pessoa e
diga se ela tem 'silva' no nome. '''
print('')
print('='*25)
Nome = str(input('Digite seu Nome: ')).strip().lower().split()
Check = 'silva' in Nome
print('Possue Silva? {}'.format(Check))
print('')
