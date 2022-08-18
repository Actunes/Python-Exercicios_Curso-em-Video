'''desenvolva um programa que pergunta a distancia
de uma viagem em km.
Calcule  o preço da passagem,Cobrando r$0,50 por km
para viagens de até 200km e R$0,45 para viagen
mais longas.'''

from termcolor import colored , cprint
print('')
print('='*25)
print('')
Distancia_viagem = float(input(colored('Digite a distancia percorrida: ','red')))
if Distancia_viagem <= 200:
    Preço = Distancia_viagem * 0.50 
else: 
    Preço = Distancia_viagem * 0.45
print('')
print('O preço de sua passagem ficou R${:.2f}'.format(Preço))