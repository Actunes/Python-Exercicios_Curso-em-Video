#Faça um algoritmo que leia o preço de um produto e mostre seu novo
#preço com 5% de desconto.
print('')
print('='*25)
Preço = float(input('Preço do Produto: R$'))
Preço_5 = Preço * 0.05
Preço_Total = Preço - Preço_5
print('Preço com 5% de desconto: R${:.2f}'.format(Preço_Total))
print('='*25)
print('')