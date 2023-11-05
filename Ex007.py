# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
# Erros cometidos:
# Digitei com , invés de .
# Tentei com int mas não considerava número decimais

n1 = float(input('Quanto você tirou na prova 1 de matemática?\n'))
n2 = float(input('Quanto você tirou na prova 2 de matemática\n'))
n3 = (n1+n2)/2
print('A média da suas notas é {:.2f}.'.format(n3))