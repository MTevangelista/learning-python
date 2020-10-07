"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você 
deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

price1 = float(input('Informe o preço do primeiro produto:\n'))
price2 = float(input('Informe o preço do segundo produto:\n'))
price3 = float(input('Informe o preço do terceiro produto:\n'))

if price1 < price2 and price1 < price3:
    print('Você deve comprar o primeiro produto')
elif price2 < price1 and price2 < price3:
    print('Você deve comprar o segundo produto')
else:
    print('Você deve comprar o terceiro produto')

print('FIM')