import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('Data de Abertura: {}'.format(self.data_abertura))
        print('Transações: ')
        for t in self.transacoes:
            print('-', t)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        print('Conta Inicializada')
        self.titular = cliente
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

        
    def pega_saldo(self):
        return self._saldo


    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return false
        else:
            destino.deposita(valor)
            return True
            self.historico.transacoes.append("Transferencia de {} para {}".format(valor, destino.numero))

    def extrato(self):
        print('Numero: {} \nsaldo: {}'.format(self.numero, self.saldo))
        self.historico.transacoes.append("Extrato da conta: {}".format(self.numero))