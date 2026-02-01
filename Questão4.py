# Questão 4- Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input("Preço da mercadoria: R$ "))
desconto_percentual = float(input("Percentual de desconto: "))

desconto = preco * desconto_percentual / 100
preco_final = preco - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
