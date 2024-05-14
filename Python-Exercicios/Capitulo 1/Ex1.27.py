#Ex1.27: Crie um programa que peça ao usuário para digitar o valor inicial de um investimento, a taxa de juros mensal e o número de meses que o valor ficou investido. 
#Em seguida, o programa deve calcular e mostrar o valor final do investimento, considerando o uso de juros compostos.

valor_inicial = float(input("Insira o valor inicial do investimento: "))
taxa_juros_mensal = float(input("Insira a taxa de juros mensal (em porcentagem): ")) / 100
num_meses = int(input("Insira o número de meses que o valor ficou investido: "))


valor_final = valor_inicial * (1 + taxa_juros_mensal) ** num_meses

print(f"O valor final do investimento é R$ {valor_final:.2f}.")
