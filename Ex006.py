#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

a = int(input('Digite um número\n'))
print('O número que digitou é \n{}'.format(a))
b = a*2
print('O dobro desse número é \n{}'.format(b))
c = a*3
print('O triplo desse número é \n{}'.format(c))
d = a**(1/2)
print('A raiz quadrada desse número é \n{:.2f}'.format(d))
