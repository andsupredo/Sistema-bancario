from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, ag, conta, saldo):
        self.ag = ag
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.infos()

    def infos(self):
        print(f'Agência: {self.ag} '
              f'Conta: {self.conta} '
              f'Saldo: {self.saldo} ')

    @abstractmethod
    def sacar(self, valor): pass


class ContaCorrente(Conta):
    def __init__(self, ag, conta, saldo, limite=200):
        super().__init__(ag, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente!')
            return

        self.saldo -= valor
        self.infos()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
            return

        self.saldo -= valor
        self.infos()
