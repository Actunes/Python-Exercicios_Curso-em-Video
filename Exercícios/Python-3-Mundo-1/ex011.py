#Faça um programa que leia a largura e a altura de uma parede em metros
#, calcule a sua área e a quantidade ded tinha necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2m²
print('')
print('='*25)
Largura = float(input('Largura em Metros: '))
Altura = float(input('Altura em Metros: '))
print('='*25)
Area = Largura * Altura
Quantidade = Area / 2
print('Área da parede: {}\nTinta necessária: {} Litros de tinta'.format(Area ,Quantidade))
print('')