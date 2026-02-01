# Questão 3- Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o salário: R$ "))
percentual = float(input("Digite o percentual de aumento: "))

aumento = salario * percentual / 100
novo_salario = salario + aumento

print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
