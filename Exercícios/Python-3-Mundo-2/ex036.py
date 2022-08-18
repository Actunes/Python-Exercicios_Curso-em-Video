'''Escreva um programa para aprovar o empréstimo 
bancário para a compra de uma casa.O programa 
vai perguntar o valor da casa, o salário do 
empreendedor e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salário ou então
o empréstimo será negado.'''
#imports
from time import sleep
import emoji
#Apresentation of the program
print('\033[0;32m')
print('='*25)
print(' APROVAÇÃO DE EMPRÉSTIMO')
print('='*25)
sleep(1) # sleep for 1 second
print('\033[m')
print('\033[0;35m Informações necessárias:\n[1]Valor da casa\n[2]Salário do empreendedor\n[3]Tempo de pagamento (anos)')
print('\033[m')
#input of dates from user
sleep(2) # sleep for 2 seconds
Valor_Casa = float(input('[1] Valor da casa: R$'))
Salário_Empreendedor = float(input('[2] Salário do empreendedor: R$'))
Tempo_Pagamento = int(input('[3] Tempo de pagamento (anos): '))
print('')
#installment
Prestação = Valor_Casa / (Tempo_Pagamento * 12)
#check for exceed 30%
if Prestação >= Salário_Empreendedor * 0.30:
    print(emoji.emojize('\033[0;31mPRESTAÇÃO NEGADA :xis:\033[m', language='pt'))
else: 
    print(emoji.emojize('\033[0;32mPRESTAÇÃO APROVADA :marca_de_seleção:\033[m', language='pt'))
print('')
