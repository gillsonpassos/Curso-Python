nome = 'Gilson Passos'
altura = 1.70
peso = 80
imc = peso / altura ** 2

 # "f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# gilson Passos tem 1.70 de altura
# pesa 80 quilos e seu IMC é
# 27.68166089965398