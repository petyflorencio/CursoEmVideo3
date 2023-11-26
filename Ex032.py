#Faça um programa que leia um ano qualquer e mostra se ele é BISSEXTO

year = int(input('Tell me a year\n'))
if year % 4 == 0:
    print('{} is a leap year!!!'.format(year))
else:
    print('{} is not a leap year.'.format(year))