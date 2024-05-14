#Ex 2.25: Crie um programa que peça ao usuário para inserir dois números, a e b, e uma operação aritmética (+, -, * ou /). 
#Use a estrutura match..case para avaliar uma expressão que combine a operação inserida pelo usuário e, em seguida, imprima o resultado da operação escolhida.

a = float(input("Insira o primeiro número (a): "))
b = float(input("Insira o segundo número (b): "))
operacao = input("Insira a operação aritmética (+, -, * ou /): ")

match operacao:
    case "+":
        resultado = a + b
    case "-":
        resultado = a - b
    case "*":
        resultado = a * b
    case "/":
        if b != 0:
            resultado = a / b
        else:
            print("Erro: Divisão por zero!")
            resultado = None
    case _:
        print("Operação inválida!")
        resultado = None

if resultado is not None:
    print(f"O resultado da operação {a} {operacao} {b} é: {resultado}")

