# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km você percorreu com o carro? '))
dias = float(input('Quantos dias você ficou com o carro? '))
pagar = (km * 0.15) + (dias * 60)

print('O total a pagar é de R${}'.format(pagar))
