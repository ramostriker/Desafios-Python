# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

ang = int(input('Informe um ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('O seno é {:.2f}, cosseno é {:.2f} e a tangente é {:.2f}' .format(seno, cosseno, tangente))
