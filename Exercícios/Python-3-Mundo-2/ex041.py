'''A confederação nacional de natação precisa 
de um programa que leia o ano de nascimento de um 
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER
'''
from datetime import date
from time import sleep
print('\033[0;35m')
print('='*25)
print(' Definição de categoria')
print('='*25)
print('\033[m')
sleep(0.5)
year = date.today().year
print('\033[0;32mTabela de categorias:\nAté 9 anos: MIRIM\nAté 14 anos: INFANTIL\nAté 19 anos: JUNIOR\nAté 20 anos: SENIOR\nAcima de 20 anos: SENIOR\033[m')
print('')
sleep(1)
year_nascimento = int(input('Ano de nascimento: '))
Categoria = year - year_nascimento
print('\033[0;34m')
if Categoria <=9:
    print('Categoria: MIRIM')
elif Categoria > 9 and Categoria <= 14:
    print('Categoria: INFANTIL')
elif Categoria > 14 and Categoria <= 19:
    print('Categoria: JUNIOR')
elif Categoria > 19 and Categoria <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
print('\033[m')
