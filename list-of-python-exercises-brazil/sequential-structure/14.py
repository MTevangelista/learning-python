# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça
# um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável 
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com 
# as mensagens adequadas.

max_weight = 50

fish_weight = float(input('Informe o peso de peixes:\n'))

if fish_weight > max_weight:
    excess_weight = fish_weight - max_weight
    penalty_value = excess_weight * 4
    print('Quantidade de quilos além do limite:', excess_weight)
    print('Valor da multa que deverá pagar:', penalty_value)
else:
    print('Quantidade de quilos está dentro do limite')

print('FIM')    