# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

height = float(input('Informe a altura de uma pessoa:\n'))
ideal_weight = 72.7 * height - 58

print("%.2f" % round(ideal_weight, 2) + ' ' + 'kg')