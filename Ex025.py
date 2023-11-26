#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Tell me your full name:\n')).strip()
print('Alright, your name is {}.'.format(name.title()))
nameTitle = name.title()
print('Is it true that your name contais "Silva"? {}'.format('Silva' in nameTitle))