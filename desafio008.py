#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input('Distancia em metros: '))
cm = medida * 100
mm = medida * 1000

print('{}m equivale a {:.0f}cm e a {:.0f}mm' .format(medida, cm, mm))
