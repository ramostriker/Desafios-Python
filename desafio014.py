# Escreva um programa que converta uma temperatuda digitada em °C e converta para °F.

c = float(input('Informe a temperatuda em °C: '))
f = 9 * c / 5 + 32
print('A temperatuda de {}°C é igual a {}°F!'.format(c, f))
