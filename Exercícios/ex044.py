'''Elabora um programa que calcule o valor a ser
pago por um produto,considerando o seu 
preço normal e condição de pagamento: 
-A vista dinheiro/cheque: 10% de desconto
-Á vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal.
-3x ou mais no cartão: 20% de juros'''


from time import sleep
print('\033[0;35m')
print('='*25)
print('  PAGAMENTO DE PRODUTO')
print('='*25)
print('\033[m')
sleep(0.5)
Valor_Produto = float(input('Valor do produto: R$'))
sleep(1)
print('')
print('\033[0;33mCondições de pagamento:\n[1] A vista dinheiro/cheque\n[2] A vista no cartão\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão.','\033[m')
sleep(0.5)
print('\033[0;96m')
Escolha_Usuario = int(input('Opção escolhida: '))
print('')
if Escolha_Usuario == 1:
    Valor_Final = Valor_Produto - (Valor_Produto * 0.10)
    print('Opção escolhida [1]\nTotal a ser pago: R$ {:.2f}'.format(Valor_Final))
elif Escolha_Usuario == 2:
    Valor_Final = Valor_Produto - (Valor_Produto * 0.5)
    print('Opção escolhida [2]\nTotal a ser pago: R$ {:.2f}'.format(Valor_Final))
elif Escolha_Usuario == 3:
    Valor_Final = Valor_Produto / 2
    print('Opção escolhida [3]\nNúmero de parcelas: 2\nTotal a ser pago por parcela: R$ {:.2f}'.format(Valor_Final))
elif Escolha_Usuario == 4:
    Parcela = int(input('Digite o número de parcelas: '))
    Valor_Final = (Valor_Produto + ( Valor_Produto * 0.20)) / Parcela
    print('Opção escolhida [4]\nNúmero de parcelas: {}\nTotal a ser pago por parcela: R${:.2f}'.format(Parcela,Valor_Final))
else:
    print('Opção invalida, tente novamente!')
print('\033[m')
