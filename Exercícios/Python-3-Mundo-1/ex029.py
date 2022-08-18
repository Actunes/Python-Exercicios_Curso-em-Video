'''Escreva um programa que leia a velocidade de um 
carro.
Se ele ultrapassar 90km/h,mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7,00 por cada km acida do limite'''

print('')
print('='*25)
print('')
Velocidade = int(input('Velocidade do carro: '))
if Velocidade > 90: 
    Multa = Velocidade * 7
    print('Voce ultrapassou 90km/h e foi multado em R${} '.format(Multa))
print('Tenha um bom dia! Diriga com segurança!')
print('')