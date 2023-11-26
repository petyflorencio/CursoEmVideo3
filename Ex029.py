#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostra uma mensagem dizendo que foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.

from math import trunc
speed = int(input("What was you speed in km/h just now?\n"))
if trunc(speed) >80:
    print('The speed limit for this area is 80 km/h.')
    print('You were {} km/h faster than this'.format(speed - 80))
    print('You will have to pay R$ {}'.format((speed - 80)*7))
else:
    print('Nice. Keep respecting the speed limit and drive safe.')