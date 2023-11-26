#Crie um programa que leia um número inteiro e mostra ne tela se ele é par ou impar.

num = int(input('Tell me a number:\n'))
result = num % 2

#Resto da divisão significa impar, sem resto significa par

if result == 0:
    print('Your number {} is even.'.format(num))
else:
    print('Your number {} is odd.'.format(num))