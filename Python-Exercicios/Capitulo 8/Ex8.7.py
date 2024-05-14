#Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa, 
#e um método mostrar_dados que exiba o nome e a idade da pessoa. 
#Crie uma classe chamada Funcionario que herde da classe Pessoa e adicione um 
#atributo salario e um método chamado mostrar_dados que exiba o nome, 
#a idade e o salário do funcionário. Crie uma lista com duas pessoas e dois 
#funcionários e faça um laço para chamar o método mostrar_dados de todos os objetos dessa lista.


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Salário: R${self.salario}")


pessoa1 = Pessoa("Carlos", 16)
pessoa2 = Pessoa("Maria", 25)
funcionario1 = Funcionario("Pedro", 43, 3000)
funcionario2 = Funcionario("Ana", 28, 3500)

lista_pessoas = [pessoa1, pessoa2, funcionario1, funcionario2]

for pessoa_ou_funcionario in lista_pessoas:
    pessoa_ou_funcionario.mostrar_dados()
