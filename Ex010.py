# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar
# Considerar 1 USD = 3.27 BRL

# Erros: utilizar , invés de . na divisão para converter

money = float(input('Quantos reais você tem atualmente?\n R$'))
usd = money/3.27
print('Que legal, R$ {} equivale a U$ {:.2f}!\nTá na hora de visitar Kahmarão, em? Sdds dólar nesse preço'
      .format(money,usd))
