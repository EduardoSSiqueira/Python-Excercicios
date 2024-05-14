#Faça um programa que use List Comprehension para criar uma lista com os
# números divisíveis por 3 ou 5 de 0 a 30.

divisiveis_por_3_ou_5 = [num for num in range(31) if num % 3 == 0 or num % 5 == 0]

print("Números divisíveis por 3 ou 5 de 0 a 30:", divisiveis_por_3_ou_5)
