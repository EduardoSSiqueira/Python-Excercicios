
#Exercicio 1.25 :: Crie um programa que leia o nome, o salário e o valor do imposto de uma pessoa como entrada e imprima, 
#ao fim, uma saída no seguinte formato: "Fulano tem um salário líquido de R$ 1.800,00.". 
#Observe a formatação do salário.


nome = input("Qual seu nome: ")
salario = float(input("S5alário da pessoa: "))
imposto = float(input("Digite o valor do imposto da pessoa: "))
salario_liquido = salario - imposto
print("{} tem um salário líquido de R$ {:.2f}.".format(nome, salario_liquido))

