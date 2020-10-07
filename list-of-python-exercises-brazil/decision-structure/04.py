# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letter = str(input('Informe uma letra:\n')).lower()

vogais = 'aeiou'

if len(letter) > 1:
    print('Erro, informe apenas uma letra!')
elif letter in vogais:
    print('É vogal')
else:
    print('É consoante')

print('FIM')