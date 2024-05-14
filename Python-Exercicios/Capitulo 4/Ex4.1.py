#Crie um programa que peça ao usuário para inserir dois números e calcule a potência do primeiro 
#número pelo segundo número.

def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado

base = float(input("Digite o primeiro número (base): "))
expoente = float(input("Digite o segundo número (expoente): "))

potencia = calcular_potencia(base, expoente)

print("O resultado de", base, "elevado a", expoente, "é:", potencia)
