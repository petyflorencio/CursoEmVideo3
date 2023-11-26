#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
choice = randint(1, 5)
num = int(input("What number, between 1 and 5, I'm thinking about?\n"))
if num == choice:
    print("That's right!!!!!!! I choose {}".format(choice))
else:
    print("That's not right........ I choose {}".format(choice))


