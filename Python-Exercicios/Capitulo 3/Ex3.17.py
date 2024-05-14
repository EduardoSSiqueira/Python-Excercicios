#Crie um programa que encontre e mostre o segundo maior e o segundo menor números em uma lista de 10 números digitada pelo usuário.

numeros = []
for i in range(10):
    numero = float(input("Inserir um número: "))
    numeros.append(numero)

numeros_ordenados = sorted(numeros)

segundo_menor = numeros_ordenados[1]
segundo_maior = numeros_ordenados[-2]

print("O segundo menor número é:", segundo_menor)
print("O segundo maior número é:", segundo_maior)
