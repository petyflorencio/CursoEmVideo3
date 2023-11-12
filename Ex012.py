# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Quantos reais custa um notebook?\n R$'))
note = (preço*5/100) + preço
print('Esse notebook pode ficar por R$ {:.2f} caso compre a vista.'.format(note))