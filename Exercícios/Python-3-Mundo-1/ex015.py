'''Escreva um programa que pergunte a quantidade de km 
percoriddos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preço a pagar
, sabendo que o carro custa R$60 por dia e R$0.15 por km
rodado'''

print('')
print('='*25)
km_rodados = int(input('Quilometros Rodados: '))
dias_alugados = int(input('Dias Rodados: '))
preço_pagar = ( km_rodados * 0.15 ) + dias_alugados * 60
print('Quilometros Rodados: {} KM\nDias Alugados: {} Dias\nTotal á ser pago: R${:.2f}'.format(km_rodados,dias_alugados,preço_pagar))
print('')