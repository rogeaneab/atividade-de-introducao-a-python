# Questãõ 8- Escreva um programa que leia três números e que imprima o maior e o menor. 

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print("Maior número:", maior)
print("Menor número:", menor)
