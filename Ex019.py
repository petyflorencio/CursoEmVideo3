#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

#Observação: assisti à resolução para usar a lib corretamente

import random
print('Kahmarão, Pety, Fabrício e Lucas, vou sortear um de vocês para apagar o quadro...')
person1 = str('Kahmarão')
person2 = str('Pety')
person3 = str('Fabrício')
person4 = str('Lucas')
lista = [person1, person2, person3, person4]
escolha = random.choice(lista)
print('O escolhido foi...\n{}!'.format(escolha))
