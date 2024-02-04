#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço do produto: '))
novo = preco - (preco *5 / 100)

print('O preço do produto com 5% de desconto é de R${}' .format(novo))
