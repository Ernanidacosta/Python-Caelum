#-*- coding: utf-8 -*-
def deposita(conta, valor):
	conta['saldo'] += valor

def saca(conta, valor):
	conta['saldo'] -= valor

def extrato(conta):
	print("Numero: {}\n saldo: {}".format([conta'numero'],[conta'saldo']))


def cria_conta(numero, titular, saldo, limite):
	conta = {"numero": numero, "titular": titular, "saldo": saldo,"limite": limite,}
	return conta
