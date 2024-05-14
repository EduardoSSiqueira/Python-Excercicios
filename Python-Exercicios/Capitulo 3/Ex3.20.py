#Crie um programa que calcule e mostre o fatorial de todos os números de 1 a n, onde n é digitado pelo usuário.

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("O número deve ser positivo.")
else:
    # Calcula e mostra o fatorial de todos os números de 1 a n
    print("Fatorial de cada número de 1 a", n, ":")
    for i in range(1, n + 1):
        print(i, "! =", calcular_fatorial(i))
