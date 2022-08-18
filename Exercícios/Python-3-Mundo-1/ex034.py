'''Escreva um programa que pergunte o salário
de um funcionario e calcule o valor do seu Aumento
Para salários a R$1250,00 calcule um Aumento de 10%
Para os inferiores ou iguais,o Aumento é de 15%'''
print('')
print('='*25)
print('')
Salário_Funcionário = float(input('Digite o Salário do funcionário: R$'))
if Salário_Funcionário < 1250:
    Aumento = 0.10
else:
    Aumento = 0.15
Salário_Aumento =   ( Salário_Funcionário / Aumento ) + Salário_Funcionário
print('O novo salário com {} de aumento será de R${:.2f}'.format(Aumento,Salário_Aumento))
print('')