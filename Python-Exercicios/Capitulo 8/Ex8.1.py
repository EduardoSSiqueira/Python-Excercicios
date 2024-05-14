#Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa. 
#Crie um método chamado mostrar_dados que exiba o nome e a idade da pessoa. 
#Crie duas instâncias da classe Pessoa e chame o método mostrar_dados de cada uma das instâncias.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

pessoa1 = Pessoa("Alice", 25)
pessoa2 = Pessoa("Bob", 30)

pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
