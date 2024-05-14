#:: Faça um programa que peça ao usuário para digitar uma lista de números e que, em seguida, use filtragem
# (filter) para retornar uma nova lista apenas com os números pares.

numeros = input("Digite uma lista de números separados por espaço: ").split()

numeros = list(map(int, numeros))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Números pares:", numeros_pares)


