# Faça um programa que leia a largura e a altura de uma parede em metros
# Calcule a sua área e a quantidade de tinta necessária para pintá-la
#
# Referência:
# Cada litro de tinta pinta uma área de 2m²
# Área = largura * altura

lar = float(input('Quantos metros de altura tem sua parede?\n'))
alt = float(input('Quantos metros de largura tem sua parede?\n'))
area = lar*alt
print('Legal, então a área total são {:.2f} m².'.format(area))
tinta = area/2
print ('Precisaremos de {:.2f} litros de tinta para conseguir pintar tudo.'.format(tinta))