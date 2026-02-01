# Questão 7- Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = float(input("Velocidade do carro (km/h): "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado!")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite.")
