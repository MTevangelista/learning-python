# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo inválido.

letter = str(input('Informe uma letra:\n')).upper()

if letter == 'M':
    print('Masculino')
elif letter == 'F':
    print('Feminino')
else:
    print('Sexo inválido')

print('FIM')