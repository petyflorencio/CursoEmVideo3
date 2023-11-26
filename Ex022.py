#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maísculas
#O nome com todas minúsculas
#Quantas letras ao todo, sem espaços
#Quantas letras tem o primeiro nome

fullName = str(input("What's your full name, bitch?\n")).strip()
upperName = fullName.upper()
lowerName = fullName.lower()
nameCount = len(fullName) - fullName.count(' ')
fnameCount = fullName.find(' ')

print('Thank you {}.'.format(fullName))
print('Your name in upper case is {}.'.format(upperName))
print("In lower case would be {}.".format(lowerName))
print('This name contains {} letters.'.format(nameCount))
print('Your first name contains {} letters.'.format(fnameCount))