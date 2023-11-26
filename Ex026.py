#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

phrase = str(input('Write me a phrase.\n')).strip()
print('Alright, your phrase is {}'.format(phrase))

lower = phrase.lower()
print('This phrase contains {} letters "a".'.format(lower.count('a')))
print('First time it appears is in the {}º position.'.format(lower.find('a')+1))
print('Last time it appears is in the {}º position.'.format(lower.rfind('a')+1))
