#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar
print('='*25)
Reais = float(input('Valor em Reais: R$ '))
Conversao_dolares = Reais / 5.65
print('Reais: R${}'.format(Reais))
print('Convertido em Dólares: ${:.2f}'.format(Conversao_dolares))
print('='*25)