#Crie uma classe chamada ContaBancaria com os métodos depositar e sacar. 
#Utilize tratamento de exceções para lidar com saques maiores que o saldo disponível, 
#criando uma exceção personalizada.

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        super().__init__(f"Saldo insuficiente. Saldo atual: R${saldo_atual:.2f}, Valor do saque: R${valor_saque:.2f}")

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor

try:
    minha_conta = ContaBancaria("João", 1000)
    minha_conta.depositar(500)
    minha_conta.sacar(1500) 
except SaldoInsuficienteError as e:
    print(e)
