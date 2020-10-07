# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

value = float(input('Informe um valor:\n'))

if value < 0:
    print('O valor é negativo')
elif value > 0:
    print('O valor é positivo')
else:
    print('O valor é nulo')

print('FIM')