# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# - A) o produto do dobro do primeiro com metade do segundo .
# - B) a soma do triplo do primeiro com o terceiro.
# - C) o terceiro elevado ao cubo.

nInt1 = int(input('Informe um número inteiro:\n'))
nInt2 = int(input('Informe outro número inteiro:\n'))
nReal3 = float(input('Informe um número real:\n'))

a = nInt1 * 2 + nInt2 / 2
b = nInt1 * 3 + nReal3
c = nReal3 ** 2

print('O produto do dobro do primeiro com metade do segundo é:', a)
print('A soma do triplo do primeiro com o terceiro é:', b)
print('O terceiro elevado ao cubo é:', c)