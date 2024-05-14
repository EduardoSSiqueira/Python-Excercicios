#Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa. 
#Crie um método chamado mostrar_dados que exiba o nome e a idade da pessoa. 
#Crie uma classe chamada Cliente que herde da classe Pessoa e adicione um atributo chamado endereco. 
#Crie um método chamado mostrar_dados na classe Cliente que exiba o nome, a idade e o endereço do cliente. 
#Crie uma instância da classe Cliente e chame o método mostrar_dados.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Endereço: {self.endereco}")


cliente = Cliente("Carlos", 35, "Rua das Flores, 123")
cliente.mostrar_dados()
