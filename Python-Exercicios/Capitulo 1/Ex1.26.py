#Ex 1.26: Crie um programa que peça ao usuário para digitar a altitude inicial de um objeto em queda livre a partir do repouso. 
#Em seguida, o programa deve calcular e mostrar o tempo que o objeto leva para atingir o solo, desconsiderando a resistência do ar.

import math


altura_inicial = float(input("Digite a altitude inicial do objeto em metros: "))

gravidade = 9.81 

tempo = math.sqrt((2 * altura_inicial) / gravidade)

print(f"O objeto leva {tempo:.2f} segundos para atingir o solo.")

