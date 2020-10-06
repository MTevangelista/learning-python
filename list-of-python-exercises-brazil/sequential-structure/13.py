# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# - Para homens: (72.7*h) - 58
# - Para mulheres: (62.1*h) - 44.7

height = float(input('Informe a altura de uma pessoa:\n'))

ideal_weight_for_men = (72.7 * height) - 58
ideal_weight_for_women = (62.1 * height) - 44.7

print(
    'Peso ideal para homens é: ' + 
    "%.2f" % round(ideal_weight_for_men, 2) + ' ' + 'kg'
)

print(
    'Peso ideal para mulheres é: ' +
    "%.2f" % round(ideal_weight_for_women, 2) + ' ' + 'kg'
)