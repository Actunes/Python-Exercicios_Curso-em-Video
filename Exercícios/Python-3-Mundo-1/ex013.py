#Faça um algoritmo que leia o salário de um funcionário e mostre seu
#novo salário, com 15% de aumento.
print('')
print('='*25)
Salário = float(input('Salário do Funcionário: '))
novo = Salário + (Salário * 0.15)
print('Novo salário : {:.2f}'.format(novo))
print('')