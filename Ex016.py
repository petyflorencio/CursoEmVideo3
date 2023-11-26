#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: digite um número: 6.127
#O número 6.127 tem a parte inteira 6

import math
num = float(input('Digite um número real aleatório (Ex: 9.2367)\n'))
numint = math.trunc(num)
print('O numero que digitou foi {}.\n'
      'A porção inteira do seu número é: {}.'.format(num,numint))