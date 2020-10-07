# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Informe o primeiro número:\n'))
n2 = float(input('Informe o segundo número:\n'))
n3 = float(input('Informe o terceiro número:\n'))

print(f'O maior é: {max(n1, n2, n3)}')
print(f'O menor é: {min(n1, n2, n3)}')

print('FIM')