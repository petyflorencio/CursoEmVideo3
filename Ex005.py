#Faça um programa que leia um número inteiro e mostre na tela o seu sucesso e seu antecessor

a= int(input('Olá querida, espero que esteja bem de boa!\n'
             'Me diz ai um número inteiro por favor\n'))
print('O número que antecede o que digitou é {}\n'
      'E o que vem logo após o que digitou é {}'.format((a-1),(a+1)))
