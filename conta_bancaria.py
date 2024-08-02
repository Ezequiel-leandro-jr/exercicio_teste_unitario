class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, quantia):
        if quantia <= 0:
            raise ValueError("A quantia de depósito deve ser positiva")
        self.saldo += quantia
        return quantia

    def sacar(self, quantia):
        if quantia > self.saldo:
            raise ValueError("Fundos insuficientes")
        self.saldo -= quantia
        return quantia

    def obter_saldo(self):
        return self.saldo

    def obter_titular(self):
        return self.titular

if __name__ == "__main__":
    # Exemplo de uso
    conta = ContaBancaria("Alice", 100)
    print(conta.obter_titular())  # Alice
    print(conta.obter_saldo())  # 100
    conta.depositar(50)
    print(conta.obter_saldo())  # 150
    conta.sacar(30)
    print(conta.obter_saldo())  # 120