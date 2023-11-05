#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
#todas as informações possíveis sobre ele

n1 = (input('Digite algo\n'))
print('Você digitou {}\n'.format(n1))
print('O tipo primito do que você digitou é\n',type(n1))

print('O que você escreveu é um caractere?', n1.isalpha())
print('O que você escreveu é um número?', n1.isnumeric())
print('O que você escreveu é um dígito?', n1.isdigit())
print('O que você escreveu é um caractere ou um número?', n1.isalnum())
print('O que você escreveu é uma decimal?', n1.isdecimal())
print('O que você escreveu está em minúsculo?', n1.islower())
print('O que você escreveu está em caixa alta?', n1.isupper())
print('O que você escreveu é capitalizada (maiúsculas e minúsculas)?', n1.istitle())
print('O que você escreveu é um espaço?', n1.isspace())
print('O que você escreveu é printável?', n1.isprintable())