# Faça um programa que leia a largua e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

larguram = float(input('Qual a largura da parede? '))
alturam = float(input('Qual a altura da parede? '))
area = larguram * alturam
tinta = area / 2

print('Para pintarmos {}m², precisaremos de {} litros de tinta' .format(area, tinta))
