#Faça um programa que leia o cromprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#Calcule e mostre o comprimento da hipotenusa

#Erros: não consegui colocar .:2f na máscara

import math
base = float(input('Me diga quanto mede a base do seu triângulo retângulo: '))
altura = float(input('Me diga quanto mede a altura do seu triângulo retângulo: '))
hip = math.hypot(base, altura)
print('A hipotenusa do seu triângulo equivale a {}.'.format(hip))
