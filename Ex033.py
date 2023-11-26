#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

a = int(input('Tell me the first number:\n'))
b = int(input('Tell me the second number:\n'))
c = int(input('Tell me the third number:\n'))

lowest = a
if b<a and b<c:
    lowest = b
if c<a and c<b:
    lowest = c

higher = a
if b>a and b>c:
    higher = b
if c>a and c>b:
    higher = c
print('The lowest value is {}.'.format(lowest))
print('The highest value is {}.'.format(higher))
