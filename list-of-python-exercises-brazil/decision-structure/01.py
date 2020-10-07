# Faça um Programa que peça dois números e imprima o maior deles

n1 = float(input('Informe um número:\n'))
n2 = float(input('Informe outro número:\n'))

if n1 > n2:
    print(f'O maior número é: {n1}')
elif n2 > n1:
    print(f'O número maior é: {n2}')
else:
    print('Os números são iguais')

print('FIM')