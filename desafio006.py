# Crie um algoritmo que leia  um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raizq = n1 ** (1/2)

print('O número {} tem o dobro {}, o triplo {}, e a raiz quadrada {:.2f}.'.format(n1, dobro, triplo, raizq))
