# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trinângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catop = float(input('Informe o comprimento do cateto oposto: '))
catad = float(input('Informe o comprimento do cateto adjacente: '))
hyp = hypot(catop, catad)

print('Com o comprimento do cateto oposto de {} e do cateto adjacente de {}, a Hypotenusa vai medir {:.2f}'.format(catop, catad, hyp))
