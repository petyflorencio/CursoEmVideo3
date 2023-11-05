# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

# Dificuldades: perder as contas das máscaras {}, tentei colocar números dentro {1} mas dava erro ao executar

# Resolução (mais fácil): print('{} x {} = {}'.format(num, 1, num*1)

n1 = int(input('Digite um número inteiro e te direi toda a tabuada dele\n'))
n2 = n1*2
n3 = n1*3
n4 = n1*4
n5 = n1*5
n6 = n1*6
n7 = n1*7
n8 = n1*8
n9 = n1*9
n10 = n1*10
print('Muito que bem, a tabuada de {} é {}, {}, {}, {}, {}, {}, {}, {} e {}'
      .format(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))
