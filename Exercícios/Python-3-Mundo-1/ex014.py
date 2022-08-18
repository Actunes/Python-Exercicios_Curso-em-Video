#Escreva um programa que converta uma temperatura digitada
# em C para F

print('')
print('='*25)
Celsius = float(input('Temperatura em °C: '))
Fahrenheit = (Celsius * (9/5) ) +32 
print('Temperatura : {:.2f}°F'.format(Fahrenheit))
print('')
print('='*25)