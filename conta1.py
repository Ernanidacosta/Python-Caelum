from conta import Conta
conta = Conta( 'Jose','123-4', 120.0, 1000.0)
print(conta.numero)

conta.deposita(20.0)
conta.extrato()
conta.saca(15)
conta.extrato()