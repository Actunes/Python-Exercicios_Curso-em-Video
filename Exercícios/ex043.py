'''Desenvolva uma lógica que leia o peso e a altura 
de uma pessoa, Calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo: 

-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

from time import sleep
print('\033[0;35m')
print('='*25)
print('     CALCULO DE IMC')
print('='*25)
print('\033[m')
sleep(0.5)
peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    imc_resultado = 'Abaixo do peso'
elif imc < 25:
    imc_resultado = 'Peso ideal'
elif imc < 30:
    imc_resultado = 'Sobrepeso'
elif imc < 40:
    imc_resultado = 'Obesidade'
else:
    imc_resultado = 'Obesidade Mórbida'
print('Seu imc: {:.2f}\n{}'.format(imc,imc_resultado))
print('')