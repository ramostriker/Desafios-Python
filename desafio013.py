#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário? ' ))
salarionovo = salario + (salario *  15 / 100)

print('O novo salário é de {:.2f}' .format(salarionovo))
