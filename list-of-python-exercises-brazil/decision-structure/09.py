# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

for i in range(1, 4):
    numeros.append(int(input(f'Informe o {i} número:\n')))

print(numeros)
numeros.sort(reverse=True)
print(numeros)

print('FIM')