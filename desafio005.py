# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número: '))
suc = n1 + 1
ant = n1 - 1

print('O número {} tem o sucessor {} e o antecessor {}' .format(n1, suc, ant))
