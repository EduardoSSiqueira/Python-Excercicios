#Crie uma classe chamada ContaBancaria com o atributo saldo e com métodos para depositar, 
#sacar e exibir o saldo da conta. Crie uma instância da classe ContaBancaria e teste os métodos criados.


class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}")


conta = ContaBancaria()
conta.exibir_saldo()  

conta.depositar(100)
conta.exibir_saldo()  
conta.sacar(50)
conta.exibir_saldo()  
conta.sacar(70)  
