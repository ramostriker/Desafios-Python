# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis.

v1 = (input('Digite algo: '))

print('O tipo primitivo dessa valor é ', type(v1))
print('Só tem espaços? ', v1.isspace())
print('É um número? ', v1.isnumeric())
print('É alfabético? ', v1.isalpha())
print('É alfanumérico? ', v1.isalnum())
print('Está em maiusculas? ', v1.isupper())
print('Está em minusculas? ', v1.islower())
print('Está capitalizada? ', v1.istitle())




