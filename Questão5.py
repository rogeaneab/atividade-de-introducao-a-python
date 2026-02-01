# Questão 5- Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

dias = int(input("Quantidade de dias: "))
km = float(input("Quantidade de km rodados: "))

preco_dias = dias * 60
preco_km = km * 0.15
total = preco_dias + preco_km

print(f"Preço a pagar: R$ {total:.2f}")
