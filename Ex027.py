#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

name = str(input('Tell me your full name:\n')).strip()
nameList = name.split()
print('Alright, your name is {}.'.format(name.title()))

fname = nameList[0]
lname = nameList[len(nameList)-1]

print('Your first name is {}.'.format(fname.title()))
print('Your last name is {}.'.format(lname.title()))