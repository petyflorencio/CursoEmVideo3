#Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos digitos separados.
#Ex: Digito um número:1834
#unidade 4
#dezena 3
#centena 8
#milhar 1

num = int(input('Give me a number with 4 digits:\n'))
print('Alright, your number is {}.'.format(num))
n = str(num)
print('The first number is {}.'.format(n[0]))
print('The second number is {}.'.format(n[1]))
print('The third number is {}.'.format(n[2]))
print('The fourth number is {}.'.format(n[3]))