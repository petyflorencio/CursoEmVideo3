#Crie um programa que leia o nome de uma cidade e
# diga se ela começou ou não com o nome "SANTO"

city = str(input('Tell me a name of a city:\n')).strip()
print('Alright, the city your typed is {}'.format(city))
cityTitle = city.title()
print('Is it true that the city starts with "Santo"? {}'.format('Santo' in cityTitle))