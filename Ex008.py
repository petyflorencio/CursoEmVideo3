# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# Referências: 1m = 100cm = 1000 mmm

n1 = float(input('Me diga sua altura em metros\n'))
n2 = n1*100
n3 = n1*1000
print('Sua altura em metros é {}.\nEm centímetros seria {} e em milímetros {}'.format(n1,n2,n3))

