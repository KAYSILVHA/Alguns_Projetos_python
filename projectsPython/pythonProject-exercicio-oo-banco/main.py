from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Kayra Silva', "123.018.889-40", 17)

print(cliente1)

conta_da_kay = Conta(cliente1, 1200, 2000)
print(conta_da_kay.consulta_saldo())


conta_da_kay.sacar(3000)
print(conta_da_kay.consulta_saldo())