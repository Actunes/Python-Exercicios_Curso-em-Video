'''Crie um programa que leia o nome de uma cidade e
diga se ela comeca ou não com o nome 'santo' '''

print('')
print('='*25)
Nome_Cidade = str(input('Digite o nome da cidade: ')).strip().lower()
Nome_Cidade_Santo = 'santo ' in Nome_Cidade
print('Cidade começa com Santo? {}'.format(Nome_Cidade_Santo))
print('')
