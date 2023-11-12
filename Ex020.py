#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Observação: assisti à resolução para usar a lib corretamente

import random
print('Kahmarão, Pety, Fabrício e Lucas, vou sortear a ordem de apresentação de vocês...')
person1 = str('Kahmarão')
person2 = str('Pety')
person3 = str('Fabrício')
person4 = str('Lucas')
lista = [person1, person2, person3, person4]
random.shuffle(lista)
print('A ordem de apresentação, da direita para a esquerda, é a seguinte...\n')
print(lista)